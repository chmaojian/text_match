# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import xlrd

import matplotlib

path = './Zk5902.csv'
f = open(path, encoding='utf-8')
data = []
for li in f.readlines():
    li = li.strip('\n')
    data.append(li)

# print(data)

re = []
for it in data:
    it = it.split(',')
    re.append(it)
re = np.asarray(re)
# print(re)
r1 = np.zeros((12, len(re)))

for i in range(len(re)):
    for j in range(12):
        r1[j][i] = re[i][j]

print(r1)

x = [i for i in range(len(re))]
y1 = r1[0]
y2 = r1[1]
y3 = r1[2]
y4 = r1[3]
y5 = r1[4]
y6 = r1[5]
y7 = r1[6]
y8 = r1[7]
y9 = r1[8]
y10 = r1[9]
y11 = r1[10]
y12 = r1[11]

# print(type(r1[0]))
# print(r1[0])
# print(y1)

# # 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots()

ax.xaxis.tick_top()
ax.invert_yaxis()

plt.subplot(1, 2, 1)

# 画水平直方图

l12 = plt.barh(x, y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12, color='r')
l11 = plt.barh(x, y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11, color='g')
l10 = plt.barh(x, y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10, color='b')
l9 = plt.barh(x, y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9, color='blanchedalmond')
l8 = plt.barh(x, y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8, color='aqua')
l7 = plt.barh(x, y1 + y2 + y3 + y4 + y5 + y6 + y7, color='aqua')
l6 = plt.barh(x, y1 + y2 + y3 + y4 + y5 + y6, color='y')
l5 = plt.barh(x, y1 + y2 + y3 + y4 + y5, color='m')
l4 = plt.barh(x, y1 + y2 + y3 + y4, color='c')
l3 = plt.barh(x, y1 + y2 + y3, color='r')
l2 = plt.barh(x, y1 + y2, color='b')
l1 = plt.barh(x, y1, color='r')
# 设置
plt.title("水平直方图")
# 设置x，y轴标签
plt.xlabel('特征重要程度')
plt.ylabel('深部/*100m')
# 设置注解狂图示
plt.legend(handles=[l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12],
           labels=['角闪石', '斜长石', '石英', '云母', '碳酸盐（矿物）', '暗色矿物', '黄铁矿', '黑云母', '石榴子石', '绿帘石', '钠长石', '碳酸盐'], loc='best')
# 显示


# plt.subplot(122)
# x1 = [1, 2, 3, 4]
# x2 = [1, 2, 3, 4]
# x3 = [1, 2, 3, 4]
#
# y1 = [4, 2, 4, 5]
# y2 = [2, 4, 0.5, 0]
# y3 = [0.5, 1, 3, 5]
# # 画水平直方图
# y1 = np.array(y1)
# y2 = np.array(y2)
# y3 = np.array(y3)

#
# l3 = plt.barh(x3, y1 + y2 + y3, color='r')
# l2 = plt.barh(x2, y2 + y1, color='b')
# l1 = plt.barh(x1, y1, color='g')
# # 设置
# plt.title("水平直方图")
# # 设置x，y轴标签
# plt.xlabel('特征重要程度')
# plt.ylabel('深部/*100m')
# # 设置注解狂图示
# plt.legend(handles=[l1, l2, l3], labels=['A岩石', 'B岩石', 'C岩石'], loc='best')
# plt.show()
