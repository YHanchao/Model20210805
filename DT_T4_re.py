from sklearn.metrics import accuracy_score,f1_score,recall_score,precision_score
from sklearn import tree
import pandas as pd
import numpy as np

# 读取数据与预先处理
newL = []

useList = ['品牌类型', 'PCA'] + ['B16', 'B17', 'B15', 'B11', 'B13', 'B3', 'B2', 'B12', 'B14']
# useList = ['品牌类型', 'PCA'] + ['B{}'.format(i) for i in range(1, 18)]
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

# X = df[['品牌类型', 'B16', 'B17', 'B15', 'B11', 'B13', 'B3', 'B2', 'B12', 'B14']].values
# X = df[list(['a{}'.format(i) for i in range(1, 9)])].values
X = df[useList].values
y = df['购买意愿'].values

def cal_prob(data, num):
    global X, y
    n = 0
    nums = np.array([-0.35052756581444017, -0.3634850427685319, -0.33490475542161724,
        -0.3584034911899144, -0.35780027944370135, -0.3553634343740415,
        -0.3556601815862112, -0.3515628199349126])
    data[list(['a{}'.format(i) for i in range(1, 9)])] *= 1 + num/100.0
    data['PCA'] = np.dot(data[list(['a{}'.format(i) for i in range(1, 9)])].values, nums)
    data = data[useList]
    data=np.array([data.tolist()])
    
    for j in range(1000):
        shuffled_index = np.random.permutation(len(df))
        X = X[shuffled_index, :]
        y = y[shuffled_index]
        split_index = int(len(df) * 0.7)
        X_train = X[:split_index, :]
        y_train = y[:split_index]

        dt = tree.DecisionTreeClassifier()
        dt.fit(X_train, y_train)
        data.reshape(1, -1)
        pred = dt.predict(data)
        n += pred[0]
    print('prob', n/1000.0)
    return n/1000.0

testDf = pd.read_csv('Data\\testData_T4.csv')
testDf['B8'] = [2021-k for k in list(testDf['B10'])]

# 开始搜寻

def search(left, right, depth):
    if depth < 8:
        m = cal_prob(testDf.loc[14], (left+right)/2)
        l = cal_prob(testDf.loc[14], left)
        r = cal_prob(testDf.loc[14], right)

        print(l,m,r)
        print(left,(left+right)/2, right)
        if(l<0.75 and m>=0.75 and r>=0.75):
            return search(left, (left+right)/2, depth+1)
        elif(l<0.75 and m<0.75 and r>=0.75):
            return search((left+right)/2, right, depth+1)
        
        
    else:
        return right, cal_prob(testDf.loc[14], right)

a = search(2,3,0)
print(a)