# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import xlrd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

from matplotlib import mlab
from matplotlib import rcParams

path = './Zk59021.csv'
f = open(path, encoding='utf-8')
data = []
for li in f.readlines():
    li = li.strip('\n')
    data.append(li)
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
# print(r1.shape)

# # 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def figure(start):
    y = [i for i in range(12)]
    m = start[0]
    for j, k in zip(start[1:6], [1, 2, 3, 4, 5]):
        for i in range(12):
            y[i] = r1[i][m:j]

        x = [i for i in range(j - m)]
        m = j

        l12 = ax.bar(x, y[0] + y[1] + y[2] + y[3] + y[4] + y[5] + y[6] + y[7] + y[8] + y[9] + y[10] + y[11], zs=k,
                     zdir='y', color='#DEB887', alpha=0.8)
        l11 = ax.bar(x, y[0] + y[1] + y[2] + y[3] + y[4] + y[5] + y[6] + y[7] + y[8] + y[9] + y[10], zs=k, zdir='y',
                     color='#00FFFF', alpha=0.8)
        l10 = ax.bar(x, y[0] + y[1] + y[2] + y[3] + y[4] + y[5] + y[6] + y[7] + y[8] + y[9], zs=k, zdir='y',
                     color='#B8860B', alpha=0.8)
        l9 = ax.bar(x, y[0] + y[1] + y[2] + y[3] + y[4] + y[5] + y[6] + y[7] + y[8], zs=k, zdir='y', color='#008B8B',
                    alpha=0.8)
        l8 = ax.bar(x, y[0] + y[1] + y[2] + y[3] + y[4] + y[5] + y[6] + y[7], zs=k, zdir='y', color='#5F9EA0',
                    alpha=0.8)
        l7 = ax.bar(x, y[0] + y[1] + y[2] + y[3] + y[4] + y[5] + y[6], zs=k, zdir='y', color='#7FFF00', alpha=0.8)
        l6 = ax.bar(x, y[0] + y[1] + y[2] + y[3] + y[4] + y[5], zs=k, zdir='y', color='#6495ED', alpha=0.8)
        l5 = ax.bar(x, y[0] + y[1] + y[2] + y[3] + y[4], zs=k, zdir='y', color='#000000', alpha=0.8)
        l4 = ax.bar(x, y[0] + y[1] + y[2] + y[3], zs=k, zdir='y', color='#FF7F50', alpha=0.8)
        l3 = ax.bar(x, y[0] + y[1] + y[2], zs=k, zdir='y', color='#0000FF', alpha=0.8)
        l2 = ax.bar(x, y[0] + y[1], zs=k, zdir='y', color='#8A2BE2', alpha=0.8)
        l1 = ax.bar(x, y[0], zs=k, zdir='y', color='#DC143C', alpha=0.8)

    ax.set_xlabel('深部/*100m')
    ax.set_ylabel('钻孔')
    ax.set_zlabel('特征重要程度')
    # 设置注解狂图示
    plt.legend(handles=[l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12],
               labels=['角闪石', '斜长石', '石英', '云母', '碳酸盐（矿物）', '暗色矿物', '黄铁矿', '黑云母', '石榴子石', '绿帘石', '钠长石', '碳酸盐'],
               loc='best')

    plt.show()


if __name__ == '__main__':
    start = [0, 6, 8, 16, 32, 34, 64, 74, 130, 144, 160, 190, 212, 294, 344, 392, 484, 552, 568, 606, 634, 658, 670,
             736, 754, 788, 820, 838, 876, 896, 922, 962, 982, 998, 1014, 1032]
    for num in range(7):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # print(start[5*num:5*num+6])
        figure(start[5 * num:5 * num + 6])
