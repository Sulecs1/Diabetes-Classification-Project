import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

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

grab_col_names(df)
check_df(df)

df.isnull().sum()
#ısı haritası kullanarak değişkenlerin birbirlerine göre korelasyon durumları incelendi
corr = df.corr()
print(corr)

#Isı haritasında, daha parlak renkler daha fazla korelasyonu gösterir.
# Tablodan ve ısı haritasından da görebileceğimiz gibi, glikoz seviyeleri, yaş, vücut kitle indeksi ve gebelik sayısı, sonuç değişkeni ile önemli bir korelasyona sahiptir. Ayrıca yaş ve gebelikler veya insülin ve cilt kalınlığı gibi özellik çiftleri arasındaki korelasyona dikkat ediniz.
sns.heatmap(corr,
         xticklabels=corr.columns,
         yticklabels=corr.columns)
plt.show()

df.hist(bins=20,color = "#1c0f45",edgecolor='orange',figsize = (15,15));
plt.show()

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



