import matplotlib.pyplot as plt
import sklearn.decomposition as dp
from sklearn.preprocessing import scale
import pandas as pd
import numpy as np

allDf = pd.read_csv('Data\\process2.csv')

# x = allDf[['B{}'.format(i) for i in range(1,18)]]
x = allDf[['a{}'.format(i) for i in range(1, 9)]]
x = scale(x.values)
y = allDf['购买意愿']

pca = dp.PCA()
reduce_x = pca.fit_transform(x)

# print(reduce_x)

print(pca.explained_variance_) # 输出特征根
print(pca.explained_variance_ratio_) # 输出解释方差比
print(pca.components_) # 输出主成分