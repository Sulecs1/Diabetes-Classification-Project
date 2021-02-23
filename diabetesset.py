import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

import pickle
from helpers.data_prep import *
from helpers.eda import *


pd.pandas.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 170)


def load():
    data = pd.read_csv("datasets/titanic.csv")
    return data

df = load()
