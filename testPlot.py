import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Data\\chi2.csv')

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimSun']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
sns.set_palette("husl")
plt.style.use('ggplot')
'''
ffig =  plt.figure(figsize=(8, 6))
fig, axes = plt.subplots(2, 4)
axes = axes.flatten()

t = 0

for i in range(1, 9):
    titles = ['电池技术性能', '舒适性', '经济性',
        '安全性', '动力性', '驾驶操控性',
        '外观内饰', '配置与质量品质']
    sns.histplot(df['a{}'.format(i)], bins=10, stat='probability', kde=True, ax=axes[t])
    plt.xlabel('')
    axes[i-1].set_title(titles[t])
    t+=1

plt.xlabel('')
ffig.tight_layout()
plt.savefig('Fig\\BigHistPlot.png', bbox_inches='tight')
plt.show()
'''
'''
for i in range(1, 8):
    for j in range(i+1, 9):
        print('a{} - a{}: {}'.format(i, j, np.corrcoef(df['a{}'.format(i)].values, df['a{}'.format(j)].values)))
'''
sns.lineplot(x='Q', y='p-Value', data=df, markers='x')
plt.xlabel('问题编号')
plt.ylabel('p值')
plt.title('$\chi^2$检验：$p-$Value')
plt.show()