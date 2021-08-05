import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

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
    plt.savefig('Fig\\preFig' + i + '.png')
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

# 数据可视化
# ax部分绘制直方图
def carScoreFig(name, ntype):
    titles = ['电池技术性能满意度得分', '舒适性整体表现满意度得分', '经济性整体满意度得分',
        '安全性表现整体满意度得分', '动力性表现整体满意度得分', '驾驶操控性表现整体满意度得分',
        '外观内饰整体表现满意度得分', '配置与质量品质整体满意度得分']
    t = 0
    for i in list(allDf)[2: 10]:
        distance = 10   # 组距
        group_num = int((max(name[i]) - min(name[i])) / distance)
        plt.hist(name[i], bins=group_num)
        plt.xlabel('分数')
        plt.ylabel('人数')
        plt.title(titles[t])
        plt.savefig('Fig\\carScore\\' + str(ntype) + '\\' + i + '.png')
        plt.close()
        t += 1

carScoreFig(dfType1, 1)
carScoreFig(dfType2, 2)
carScoreFig(dfType3, 3)

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
    plt.hist(allDf[i])
    plt.xlabel(comment)
    plt.ylabel('人数')
    plt.title(comment)
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

# ==========描述统计部分=============
