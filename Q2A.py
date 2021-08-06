import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

allDf = pd.read_csv('Data\\process2.csv')
colName = ['a{}'.format(i) for i in range(1, 9)]

for name in colName:
    data0 = allDf[allDf['购买意愿'] == 1]
    data0 = data0[['品牌类型', name]]
    df0_1 = list(data0[data0['品牌类型'] == 1][name])
    df0_2 = list(data0[data0['品牌类型'] == 2][name])
    df0_3 = list(data0[data0['品牌类型'] == 3][name])
    proData0 = pd.DataFrame({1: pd.Series(df0_1), 2: pd.Series(df0_2), 3: pd.Series(df0_3)})
    

    data1 = allDf[allDf['购买意愿'] == 0]
    data1 = data1[['品牌类型', name]]
    df1_1 = list(data1[data1['品牌类型'] == 1][name])
    df1_2 = list(data1[data1['品牌类型'] == 2][name])
    df1_3 = list(data1[data1['品牌类型'] == 3][name])
    proData1 = pd.DataFrame({1: pd.Series(df1_1), 2: pd.Series(df1_2), 3: pd.Series(df1_3)})

    ax1 = proData1.plot(kind='box', color=dict(boxes='r', whiskers='r', medians='r', caps='r'), sharey=True)
    ax2 = proData0.plot(kind='box', color=dict(boxes='g', whiskers='g', medians='g', caps='g'), sharey=True)
    # plt.grid(True)

    
    # print(proData0)
    # quit()

    plt.title(name)
    plt.savefig('Fig\\compBoxPlot\\' + name +'.png')
    plt.close()