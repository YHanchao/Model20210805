from scipy.stats import boxcox
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimSun']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
sns.set_palette("husl")
plt.style.use('ggplot')

df = pd.read_csv('Data\\BigData_0.csv')

changeList = list(['a{}'.format(i) for i in range(1, 9)])
for i in changeList:
    print(df[i])
    df[i], _ = boxcox(df[i], lmbda=None, alpha=None)
    mu, sigma = df[i].mean(), df[i].std()

    df[i] = list([(j-mu)/sigma for j in df[i]]) # z-score
    # print(type(df[i].values))
    tmp = df[i].values * np.power(np.absolute(df[i].values), -0.1)
    # print(type(tmp), tmp)
    df[i] = tmp
# y, lambda0 = boxcox(x, lmbda=None, alpha=None)

df.to_csv('Data\\BigData.csv', index=False)
for i in list(['a{}'.format(i) for i in range(1, 9)]):
    print(df[i].skew(), df[i].kurt())

def carScoreFig(name, ntype=0):
    titles = ['电池技术性能满意度得分', '舒适性整体表现满意度得分', '经济性整体满意度得分',
        '安全性表现整体满意度得分', '动力性表现整体满意度得分', '驾驶操控性表现整体满意度得分',
        '外观内饰整体表现满意度得分', '配置与质量品质整体满意度得分']
    t = 0
    for i in list(df)[2: 10]:
        distance = 5   # 组距
        sns.displot(name[i], bins=10, kde=True)
        plt.xlabel('分数')
        plt.ylabel('人数')
        plt.title(titles[t])
        # plt.text(2, 8, '$\mu=${},$\sigma=${}'.format(round(mu, 3), round(sigma, 3)))
        plt.savefig('Fig\\tmp\\' + i + '.png')
        plt.close()
        t += 1

carScoreFig(df)