import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import missingno as msno

import pickle
from helpers.data_prep import *
from helpers.eda import *
from helpers.helpers import *


pd.pandas.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 170)


def load():
    data = pd.read_csv(r"C:\Users\Suleakcay\PycharmProjects\pythonProject6\data\diabetes.csv")
    return data

df = load()

def data_understand(df):
    print("DF SHAPE:", df.shape)
    print("------------------------------------------------------------------------")
    print("OUTCOME 1 DF RATIO:", len(df[df["Outcome"] == 1]) / len(df))
    print("OUTCOME 0 DF RATIO:", len(df[df["Outcome"] == 0]) / len(df))
    print("------------------------------------------------------------------------")
    print(df.dtypes)
    print("------------------------------------------------------------------------")
    print(df.head())
    print("------------------------------------------------------------------------")
    print(df.tail())
    print("------------------------------------------------------------------------")
    print(df.isnull().sum())
    print("------------------------------------------------------------------------")
    print(df.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)
    print("------------------------------------------------------------------------")
    # Isı haritasında, daha parlak renkler daha fazla korelasyonu gösterir.
    # Tablodan ve ısı haritasından da görebileceğimiz gibi, glikoz seviyeleri, yaş, vücut kitle indeksi ve gebelik sayısı, sonuç değişkeni ile önemli bir korelasyona sahiptir. Ayrıca yaş ve gebelikler veya insülin ve cilt kalınlığı gibi özellik çiftleri arasındaki korelasyona dikkat ediniz.

    corr = df.corr()
    print(corr)
    print("------------------------------------------------------------------------")
    sns.heatmap(corr,
                xticklabels=corr.columns,
                yticklabels=corr.columns)
    plt.show()
    print("------------------------------------------------------------------------")
    print(sns.pairplot(df));
    plt.show()
    print("------------------------------------------------------------------------")
    df.hist(bins=20, color="#1c0f45", edgecolor='orange', figsize=(15, 15));
    plt.show()
    print("------------------------------------------------------------------------")

data_understand(df)

#Aykırı değer varsa görebilmek için
msno.bar(df)
plt.show()

def cat_num_col(df):
    cat_cols = col_names = [col for col in df.columns if df[col].dtypes != "O"]
    if len(cat_cols) == 0:
        print("Kategorik değişken bulunamamktadır!")
    else:
        print(f'Kategorik değişkenler : {len(cat_cols)}')
    num_cols = [col for col in df.columns if df[col].dtypes != "O"]
    if len(num_cols) == 0:
        print("Numerik değişken bulunmamaktadır")
    else:
        print(f'Numerik değişkenler : {len(num_cols)} ')

cat_num_col(df)

def missing_values_table(df):
    na_variable = [col for col in df.columns if df[col].isnull().sum() > 0]

    n_miss = df[na_variable].isnull().sum().sort_values(ascending=False)

    ratio = (df[na_variable].isnull().sum() / df.shape[0] * 100).sort_values(ascending=False)

    missing_df = pd.concat([n_miss, np.round(ratio, 2)], axis=1, keys=['n_miss', 'ratio'])
    if len(missing_df) < 0:
        print("Aykırı değer yoktur!")
    else:
        print("\nThere are {} columns with missing values\n".format(len(missing_df)))

missing_values_table(df)
#################################
# DATA PREPROCESSING            #
#################################

df_new = df.copy()
#aşağıdaki sıfır değerlerini NAN değerleri işe değiştirdik
df_new = df_new.loc[:, "Pregnancies": "Age"].replace(0, np.nan).dropna()

#döngü ile her değişkeni gezdik burada değişkenkenlerdeki diyabet olup olmama oranına göre ortalamasını aldık
for col in df_new.columns:
    if col !="Outcome":
        print(col.upper(), "\n", "DİYABET HASTASI:", df_new.loc[df["Outcome"] == 1, col].median(), "\n",
              "ŞEKER HASTASI DEĞİL:", df_new.loc[df["Outcome"] == 0, col].median())

#Sutunlardaki sıfır değerine kırılıma ataması


def col_nan_assigment(df):
    for x in df.columns:
        for y in range(len(df)):
            if x != "Outcome":
                if df.loc[y, x] == 0:
                    if df.loc[y, "Outcome"] == 1:
                        df.loc[y, x] = df.loc[df["Outcome"] == 1, x].median()

                    else:
                        df.loc[y, x] = df.loc[df["Outcome"] == 0, x].median()

col_nan_assigment(df)
df.head()


#kaç kişinin şeker hastası olduğuna ve kaçının şeker hastası olmadığını bulmak için boxplot grafiğinden yararlanacağım
sns.countplot(x="Outcome", data=df)
plt.show()

#Yaş ile sonuç arasındaki ilişkiyi görmek için
sns.barplot(x="Outcome", y="Age", data=df)
plt.show()
#yaş ortalamasının daha yüksek olduğunu görebiliriz.

p=sns.pairplot(df, hue = 'Outcome')
plt.show()

#Dataset Preparation#
#Outcome int64
df["Outcome"] = df["Outcome"].astype('category') #tip dönüştürme işlemi
df.groupby("Outcome").agg({'Age' : 'nunique'})
#Outcome  Age
#0         51
#1         45
df["Age"] #yaşların dağılımına baktım

df.loc[(df['Age'] < 30), 'NEW_AGE_CAT'] = 'young'
df.loc[(df['Age'] >= 30) & (df['Age'] < 56), 'NEW_AGE_CAT'] = 'mature'
df.loc[(df['Age'] >= 56), 'NEW_AGE_CAT'] = 'senior'
df.head()

(df.groupby(["NEW_AGE_CAT"]).agg('count'))
#yaş aralıklarını grupladım daha sonra bu gruplara göre hasta olup olmama oranını gruplara göre gözlemledim.
df.groupby(["NEW_AGE_CAT", "Outcome"]).size().unstack(fill_value=0).apply(lambda x: x/sum(x), axis=1)

#Outcome         0     1
#NEW_AGE_CAT
#mature      0.481 0.519
#senior      0.660 0.340
#young       0.788 0.212
#sonuçlara bakılırsa gençlerin hasta olmama oranı daha azdır

df.groupby(["NEW_AGE_CAT", "Outcome"]).mean()

#####################
# ONE-HOT ENCODING  #
#####################

#Aykırı değerler
num_cols = [col for col in df.columns if len(df[col].unique()) > 18 and df[col].dtypes != "O"]
df.shape
for col in num_cols:
    replace_with_thresholds(df, col)

def one_hot_encoder(dataframe, categorical_cols, drop_first=True):
    dataframe = pd.get_dummies(dataframe, columns=categorical_cols, drop_first=drop_first)
    return dataframe

ohe_cols = [col for col in df.columns if 10 >= len(df[col].unique()) > 2]

one_hot_encoder(df, ohe_cols).head()

one_hot_encoder(df, ohe_cols, drop_first=True).head()
