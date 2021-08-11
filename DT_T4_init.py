from sklearn.metrics import accuracy_score,f1_score,recall_score,precision_score
from sklearn import tree
import pandas as pd
import numpy as np

# 读取数据与预先处理

useList = ['品牌类型', 'PCA'] + ['B16', 'B17', 'B15', 'B11', 'B13', 'B3', 'B2', 'B12', 'B14']
# 这里使用主成分分析的系数矩阵
def change2PCA(dfName):
    nums = np.array([-0.35052756581444017, -0.3634850427685319, -0.33490475542161724,
        -0.3584034911899144, -0.35780027944370135, -0.3553634343740415,
        -0.3556601815862112, -0.3515628199349126])
    
    PCAList = []
    for index, row in dfName.iterrows():
        m = row[['a{}'.format(i) for i in range(1, 9)]]
        PCAList.append(np.dot(nums, m))
    
    dfName['PCA'] = PCAList
    return dfName

df = pd.read_csv('Data\\BigData_0.csv')
df = change2PCA(df)

X = df[useList].values
y = df['购买意愿'].values

for i in range(-5, 6):
    testDf = pd.read_csv('Data\\testData_T4.csv')
    testDf['B8'] = [2021-k for k in list(testDf['B10'])]
    tmp = np.array([1 + i / 100.0] * 15)
    for k in list(['a{}'.format(m) for m in range(1, 9)]):
        testDf[k] = testDf[k].values * tmp
    testDf = change2PCA(testDf)
    testX = testDf[useList].values

    tmpNp = np.zeros(15)
    for j in range(10000):
        shuffled_index = np.random.permutation(len(df))
        X = X[shuffled_index, :]
        y = y[shuffled_index]
        split_index = int(len(df) * 0.7)
        X_train = X[:split_index, :]
        y_train = y[:split_index]
        X_test = X[split_index:, :]
        y_test = y[split_index:]

        dt = tree.DecisionTreeClassifier()
        dt.fit(X_train, y_train)
        y_train_fit = dt.predict(X_train)
        y_pred = dt.predict(X_test)
        # print('训练集acc:{}，rec:{},\n\t pre:{}, f1:{}'.format(accuracy_score(y_train, y_train_fit), recall_score(y_train, y_train_fit), precision_score(y_train, y_train_fit), f1_score(y_train, y_train_fit)))
        # print('测试集acc:{}，rec:{},\n\t pre:{}, f1:{}'.format(accuracy_score(y_test, y_pred), recall_score(y_test, y_pred), precision_score(y_test, y_pred), f1_score(y_test, y_pred)))

        testY = dt.predict(testX)
        tmpNp += testY
    
    print(i, tmpNp.tolist())

testDf['是否会购买？'] = testY

print(testY)
testDf.to_csv('Data\\T4Ans.csv', index=False)

print('原始集acc:{}，rec:{},\n\t pre:{}, f1:{}'.format(accuracy_score(tempY, tmepY_test), recall_score(tempY, tmepY_test), precision_score(tempY, tmepY_test), f1_score(tempY, tmepY_test)))