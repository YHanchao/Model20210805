import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

allDf = pd.read_excel('Data\\OriginData.xlsx')
allDf = allDf[pd.notna(allDf['品牌类型'])]  # 把原数据中1969行之后本不应该存在的数据删掉

# 数据预处理1：剔除a1到a8中超过100的数据
for i in list(allDf)[2: 10]:
    allDf = allDf[allDf[i] <= 100]
allDf = allDf[allDf['B17'] <= 100]

# 绘制箱线图
def boxPlot(name, fname):
    # plt.boxplot(column=name[2: 10], showmeans=True, labels=list(name)[2:10],showcaps=True, showbox=True)
    name.boxplot(column=list(name)[2: 10], showmeans=True)
    plt.title('各项满意度得分')
    # plt.show()
    plt.savefig('Fig\\boxPlot\\' + fname + '.png')
    plt.close()
# boxPlot(allDf, 'mainOri')

# 数据预处理2：婚姻关系修正
'''
allDf = allDf[(allDf['B6'] != 1) | (allDf['B5'] == 1)] # 剔除未婚单独居住但是家庭成员超过1, 3
allDf = allDf[(allDf['B6'] != 2) | (allDf['B5'] <= 3)]  # 剔除与父母同居但是家庭成员超过3的 1
allDf = allDf[(allDf['B6'] != 3) | (allDf['B5'] == 2)]  # 剔除二人世界但是家庭成员不为2（事先已经检查过没有1） 0
allDf = allDf[(allDf['B6'] != 3) | (pd.isna(allDf['B7']))]  # 剔除二人世界但是有小孩的 4
allDf = allDf[(allDf['B6'] != 4) | (pd.isna(allDf['B7']))]  # 剔除二人世界但是有小孩的 0
allDf = allDf[(allDf['B6'] != 5) | (pd.notna(allDf['B7']))] # 剔除已婚有小孩但是B7没数据的 0
allDf = allDf[(allDf['B6'] != 5) | (allDf['B5'] - allDf['B7'] <= 2)] # 剔除已婚有小孩不与父母同居但是人数不对应的 2
'''
# 数据预处理3：收入关系修正

tempDf1 = allDf[pd.isna(allDf['B7'])]
tempDf2 = allDf[pd.notna(allDf['B7'])]
a = len(tempDf1['B7'])
tempDf1['B7'] = [0 for i in range(a)]
allDf = tempDf1.append(tempDf2)

# 数据预处理：拆分三款汽车
dfType1 = allDf[allDf['品牌类型'] == 1]
dfType2 = allDf[allDf['品牌类型'] == 2]
dfType3 = allDf[allDf['品牌类型'] == 3]

# 数据预处理2：剔除[\mu +- 3\sigma]
def cleanTooSmall(name):
    mu = [name[i].mean() for i in list(name)[2:10]]
    sigma = [name[i].std() for i in list(name)[2:10]]
    print(mu, sigma)
    tmp = 0
    for i in list(name)[2: 10]:
        name = name[(name[i] >= mu[tmp] - 3 * sigma[tmp]) | (name[i] <= mu[tmp] + 3 * sigma[tmp])]
        tmp += 1
    return name

dfType1 = cleanTooSmall(dfType1)
dfType2 = cleanTooSmall(dfType2)
dfType3 = cleanTooSmall(dfType3)

allDf = dfType1.append(dfType2.append(dfType3))


boxPlot(allDf, 'main')
boxPlot(dfType1, 'type1')
boxPlot(dfType2, 'type2')
boxPlot(dfType3, 'type3')

dfType1.to_csv('Data\\Type1.csv', index = False)
dfType2.to_csv('Data\\Type2.csv', index = False)
dfType3.to_csv('Data\\Type3.csv', index = False)
allDf.to_csv('Data\\process.csv', index = False)


# 数据可视化
# ax部分绘制直方图
'''
def carScoreFig(name, ntype):
    titles = ['电池技术性能满意度得分', '舒适性整体表现满意度得分', '经济性整体满意度得分',
        '安全性表现整体满意度得分', '动力性表现整体满意度得分', '驾驶操控性表现整体满意度得分',
        '外观内饰整体表现满意度得分', '配置与质量品质整体满意度得分']
    t = 0
    for i in list(allDf)[2: 10]:
        distance = 5   # 组距
        group_num = int((max(name[i]) - min(name[i])) / distance)
        mu = name[i].mean()
        sigma = name[i].std()
        plt.hist(name[i], bins=group_num)
        plt.xlabel('分数')
        plt.ylabel('人数')
        plt.title(titles[t])
        # plt.text(2, 8, '$\mu=${},$\sigma=${}'.format(round(mu, 3), round(sigma, 3)))
        plt.savefig('Fig\\carScore\\' + str(ntype) + '\\' + i + '.png')
        plt.close()
        t += 1

carScoreFig(dfType1, 1)
carScoreFig(dfType2, 2)
carScoreFig(dfType3, 3)
'''

for i in list(allDf)[2: 10]:
    t = 0
    titles = ['电池技术性能满意度得分', '舒适性整体表现满意度得分', '经济性整体满意度得分',
        '安全性表现整体满意度得分', '动力性表现整体满意度得分', '驾驶操控性表现整体满意度得分',
        '外观内饰整体表现满意度得分', '配置与质量品质整体满意度得分']
    distance = 5   # 组距
    group_num = 20
    plt.hist(dfType1[i], bins=group_num, alpha = 0.5, density=True)
    plt.hist(dfType2[i], bins=group_num, alpha = 0.5, density=True)
    plt.hist(dfType3[i], bins=group_num, alpha = 0.5, density=True)
    plt.title(titles[t])
    plt.savefig('Fig\\carScore\\4'+ '\\' + i + '.png')
    plt.close()


# bx部分
def cBar(name, comment, *labelName):
    x = list(set(allDf[name]))
    y = [len(allDf[allDf[name] == l]) for l in x]
    plt.bar(x, y)
    plt.xlabel(comment)
    plt.ylabel('人数')
    plt.title(comment)
    plt.savefig('Fig\\characters\\' + name + '.png')
    plt.close()

def cPie(name, comment, labelName):
    label = list(set(allDf[name]))
    x = [len(allDf[allDf[name] == l]) for l in label]
    plt.pie(x, autopct='%.1f%%')
    plt.title(comment)
    plt.legend(labelName)
    plt.savefig('Fig\\characters\\' + name + '.png')
    plt.close()

def cHist(name, comment):
    plt.hist(allDf[name])
    plt.xlabel(comment)
    plt.ylabel('人数')
    plt.title(comment)
    mu = allDf[name].mean()
    sigma = allDf[name].std()
    plt.text(2, 8, '$\mu=${},$\sigma=${}'.format(round(mu, 3), round(sigma, 3)))
    plt.savefig('Fig\\characters\\' + name + '.png')
    plt.close()

cPie('B1', '户口情况', ('户口在老家', '户口在本城市', '表示其他'))
cHist('B2', '居住年数')
cBar('B3', '居住区域', ('市中心', '非市中心的城区', '城乡结合部', '县城', '乡镇中心地带', '农村'))
cHist('B4', '驾龄')
cPie('B5', '家庭人口数', (1,2,3,4,5,6))
cBar('B6', '婚姻情况', ('未婚，单独居住', '未婚，与父母同住', '已婚/同居无子女（两人世界）', '已婚/同居无子女（与父母同住）', '已婚，有小孩，不与父母同住', '已婚，有小孩，与父母同住', '离异/丧偶', '其他'))
cPie('B7', '孩子的数量', (0,1,2,3))
cHist('B8', '出生年份')
cBar('B9', '学历', ('未受过正式教育', '小学', '初中', '高中/中专/技校', '大专', '本科', '双学位/研究生及以上'))
cHist('B10', '工龄')
cBar('B11', '所在单位性质', ('机关单位/政府部门/基层组织', '科研/教育/文化/卫生/医疗等事业单位', '国有企业', '私营/民营企业（雇员人数在8人以上）', '外资企业', '合资企业', '个体户/小型公司（雇员人数在8人以下）', '自由职业者', '不工作'))
cBar('B12', '职位', ('高层管理者/企业主/老板', '中层管理者', '资深技术人员/高级技术人员', '中级技术人员', '初级技术人员', '资深职员/办事员', '中级职员/办事员', '个体户/小型公司业主', '自由职业者', '其他'))
cHist('B13', '家庭年收入（单位：万元）')
cHist('B14', '个人年收入（单位：万元）')
cHist('B15', '家庭可支配年收入（单位：万元）')
cHist('B16', '房贷支出占比（单位：%）')
cHist('B17', '车贷支出占比（单位：%）')

# ax部分的叠加图


# ==========描述统计部分=============
# 均值与方差
def outputDiscription(name, fname):
    mu = [name[i].mean() for i in list(name)[2: 10]]
    sigma = [name[i].std() for i in list(name)[2: 10]]
    median = [np.median(name[i]) for i in list(name)[2: 10]]
    
    with open('Data\\Discription\\' + fname + '.csv', 'w', encoding='utf-8') as f:
        f.write(',')
        f.write(','.join(list(name)[2:10]))
        f.write('\n')
        f.write('均值,')
        f.write(','.join([str(s) for s in mu]))
        f.write('\n')
        f.write('标准差,')
        f.write(','.join([str(s) for s in sigma]))
        f.write('\n')
        f.write('中位数,')
        f.write(','.join([str(s) for s in median]))
    return mu, sigma, median

type1Dis = outputDiscription(dfType1, 'type1')
type2Dis = outputDiscription(dfType2, 'type2')
type3Dis = outputDiscription(dfType3, 'type3')

# ===========层次分析===============
