from sklearn import cluster
from sklearn.metrics import adjusted_rand_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

allDf = pd.read_csv('Data\\process2.csv')

# x = allDf[['B{}'.format(i) for i in range(1,18)]]
x = allDf[['a{}'.format(i) for i in range(1, 9)]]
# x = scale(x.values)
y = allDf['购买意愿']

clst = cluster.DBSCAN();
predict_labels = clst.fit_predict(x)
print("ARI:%s"%adjusted_rand_score(y,predict_labels))
print("Core sample num:%d"%len(clst.core_sample_indices_))
