import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

allDf = pd.read_csv('Data\\OriginData.csv')
allDf = allDf[pd.notna(allDf['品牌类型'])]  # 把原数据中1969行之后本不应该存在的数据删掉


'''
# 数据可视化：频率分布直方图
for i in list(allDf)[2: -1]:
    distance = 10   # 组距
    if i[0] == 'a':
        group_num = int((max(allDf[i]) - min(allDf[i])) / distance)
        plt.hist(allDf[i], bins=group_num)
    else:
        plt.hist(allDf[i])
    plt.savefig('Fig\\' + i + '.png')
    plt.close()

'''
# 数据预处理：剔除a1到a8中超过100的数据
for i in list(allDf)[2: 10]:
    allDf = allDf[allDf[i] <= 100]
allDf = allDf[allDf['B17'] <= 100]

allDf.to_csv('Data\\process.csv', index = False)

# 数据预处理：拆分三款汽车
dfType1 = allDf[allDf['品牌类型'] == 1]
dfType2 = allDf[allDf['品牌类型'] == 2]
dfType3 = allDf[allDf['品牌类型'] == 3]

dfType1.to_csv('Data\\Type1.csv', index = False)
dfType2.to_csv('Data\\Type2.csv', index = False)
dfType3.to_csv('Data\\Type3.csv', index = False)

# ==========描述统计部分=============