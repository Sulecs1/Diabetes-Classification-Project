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


#ısı haritası kullanarak değişkenlerin birbirlerine göre korelasyon durumları incelendi
corr = df.corr()
print(corr)


sns.heatmap(corr,
         xticklabels=corr.columns,
         yticklabels=corr.columns)
plt.show()
