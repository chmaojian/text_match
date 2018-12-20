import os
import xlrd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

path = '.\save_data'
files = os.listdir(path)

for file in files:
    if not os.path.isdir(file):
        data_path = path + '/' + file
        data = xlrd.open_workbook(data_path)
        f1 = data.sheet_by_name(u'矿物')

        result = []
        for i in range(1, f1.nrows):
            result.append(f1.row_values(i))

        r1 = np.zeros((12, f1.nrows - 1))

        for i in range(f1.nrows - 1):
            for j in range(12):
                r1[j][i] = result[i][j]

        x = [i for i in range(f1.nrows - 1)]

        # print(r1,'888888')

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

        # print(r1,'888888')
        # print(y1+y2,'88888')
        # print(y2,'88888')
        # print(y3,'88888')
        # print(y4,'88888')

        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        # fig = plt.figure()
        fig, ax = plt.subplots()

        ax.xaxis.tick_top()
        ax.invert_yaxis()

        print(x)

        # 画水平直方图

        l12 = plt.barh(x, y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12, color='#DC143C')
        l11 = plt.barh(x, y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11, color='#8A2BE2')
        l10 = plt.barh(x, y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10, color='#0000FF')
        l9 = plt.barh(x, y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9, color='#FF7F50')
        l8 = plt.barh(x, y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8, color='#000000')
        l7 = plt.barh(x, y1 + y2 + y3 + y4 + y5 + y6 + y7, color='#6495ED')
        l6 = plt.barh(x, y1 + y2 + y3 + y4 + y5 + y6, color='#7FFF00')
        l5 = plt.barh(x, y1 + y2 + y3 + y4 + y5, color='#5F9EA0')
        l4 = plt.barh(x, y1 + y2 + y3 + y4, color='#008B8B')
        l3 = plt.barh(x, y1 + y2 + y3, color='#B8860B')
        l2 = plt.barh(x, y1 + y2, color='#00FFFF')
        l1 = plt.barh(x, y1, color='#DEB887')
        # 设置
        # plt.title(file.replace('.csv',''))
        # 设置x，y,z轴标签
        ax.set_xlabel(file.replace('.csv', ''))
        ax.set_ylabel('钻孔深度(从浅到深)')

        # ax.set_z('钻孔')

        # 设置注解狂图示
        plt.legend(handles=[l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12],
                   labels=['角闪石', '斜长石', '石英', '云母', '碳酸盐（矿物）', '暗色矿物', '黄铁矿', '黑云母', '石榴子石', '绿帘石', '钠长石', '碳酸盐'],
                   loc='best')
        # 保存和显示

        # plt.savefig('figure'+'/'+file.replace('.csv','.jpg'))
        plt.show()
