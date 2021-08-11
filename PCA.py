import matplotlib.pyplot as plt
import sklearn.decomposition as dp
from sklearn.preprocessing import scale
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

allDf = pd.read_csv('Data\\BigData_0.csv')

plt.rcParams['font.sans-serif'] = ['SimSun']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
sns.set_palette("husl")
plt.style.use('ggplot')

# x = allDf[['B{}'.format(i) for i in range(1,18)]]
x = allDf[['a{}'.format(i) for i in range(1, 9)]]
x = scale(x.values)
y = allDf['购买意愿']

pca = dp.PCA(n_components=8)
reduce_x = pca.fit_transform(x)

# print(reduce_x)

# print(pca.explained_variance_)          # 输出特征根
print(pca.explained_variance_ratio_.tolist())    # 输出解释方差比
print(pca.components_.tolist())                  # 输出主成分

drawD = pd.DataFrame({'序号':list(range(1,9)), '解释方差占比':pca.explained_variance_ratio_.tolist()})

sns.lineplot(x='序号',y='解释方差占比',data=drawD, markers="o")

plt.show()