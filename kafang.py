import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

def calCon(df, colName, type=0):
    if type == 0:
        alList = list(set(df[colName]))
        conList = [[], []]
        conList[0] = [len(df[(df[colName] == i) & (df['购买意愿'] == 0)]) for i in alList]
        conList[1] = [len(df[(df[colName] == i) & (df['购买意愿'] == 1)]) for i in alList]
        con = chi2_contingency(np.array(conList))
        with open('卡方.txt', 'a', encoding='utf-8') as f:
            f.write(colName)
            f.write('卡方值：{}\nP-Value：{}\n'.format(con[0], con[1]))
            buy = [len(df[(df[colName] == i) & (df['购买意愿'] == 1)]) / len(df[df[colName] == i]) for i in alList]
            t = 0
            for i in alList:
                f.write(str(i))
                f.write('：')
                f.write('%.2f%%' % (buy[t] * 100))
                f.write('，正例数：{}，总数：{}'.format(len(df[(df[colName] == i) & (df['购买意愿'] == 1)]), len(df[df[colName] == i])))
                f.write('\n')
                t+=1
            f.write('\n=============\n')
    else:
        conList = [list(df['positive']), list(df['negative'])]
        con = chi2_contingency(np.array(conList))
        with open('卡方.txt', 'a', encoding='utf-8') as f:
            f.write(colName)
            f.write('卡方值：{}\nP-Value：{}\n'.format(con[0], con[1]))
            alLen = len(df['colName'])
            colNameL = list(df['colName'])
            pL = list(df['positive'])
            nL = list(df['negative'])
            for i in range(alLen):
                f.write(colNameL[i] + '：')
                per = 0
                try:
                    per = pL[i] / (pL[i] + nL[i])
                except:
                    pass
                f.write('%.2f%%' % (per * 100))
                f.write('，正例数：{}，总数：{}\n'.format(pL[i], pL[i] + nL[i]))
            f.write('\n=============\n')

    return con

allDf = pd.read_csv('Data\\process2.csv')
testL = ['B1', 'B3', 'B5', 'B6', 'B7', 'B9', 'B11', 'B12']

for i in testL:
    calCon(allDf, i, type=0)

def cutDf(df, colName, *cut):
    cutL = cut[0]
    data = {'colName': [], 'positive': [], 'negative': []}
    data['colName'] = ['(, {}]'.format(cutL[0])]
    data['positive'] = [len(df[(df[colName] <= cutL[0]) & (df['购买意愿'] == 1)])]
    data['negative'] = [len(df[(df[colName] <= cutL[0]) & (df['购买意愿'] == 0)])]

    for i in range(1, len(cutL)):
        data['colName'].append('({}, {}]'.format(cutL[i - 1], cutL[i]))
        data['positive'].append(len(df[(df[colName] > cutL[i - 1]) & (df[colName] <= cutL[i]) & (df['购买意愿'] == 1)]))
        data['negative'].append(len(df[(df[colName] > cutL[i - 1]) & (df[colName] <= cutL[i]) & (df['购买意愿'] == 0)]))
    data['colName'].append('({}, )'.format(cutL[len(cutL) - 1]))
    data['positive'].append(len(df[(df[colName] > cutL[len(cutL) - 1]) & (df['购买意愿'] == 1)]))
    data['negative'].append(len(df[(df[colName] > cutL[len(cutL) - 1]) & (df['购买意愿'] == 0)]))

    newDf = pd.DataFrame(data)
    print(newDf)
    return calCon(newDf, colName, type=1)

B2 = cutDf(allDf, 'B2', tuple(6 * i for i in range(1, 10)))
B4 = cutDf(allDf, 'B4', tuple(3 * i for i in range(1, 10)))
# B5 = cutDf(allDf, 'B5', tuple(6 * i for i in range(1, 9)))
B8 = cutDf(allDf, 'B8', tuple(5 * i for i in range(5, 12)))
B10 = cutDf(allDf, 'B10', tuple(5 * i for i in range(1, 8)))
B13 = cutDf(allDf, 'B13', tuple(10 * i for i in range(1, 10)))
B14 = cutDf(allDf, 'B14', (10,20,30,40,50,60,70,90))
B15 = cutDf(allDf, 'B15', tuple(10 * i for i in range(1, 8)))
B16 = cutDf(allDf, 'B16', tuple(10 * i for i in range(1, 6)))
B17 = cutDf(allDf, 'B17', tuple(10 * i for i in range(1, 6)))