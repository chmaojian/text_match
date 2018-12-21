import os
import xlrd
import numpy as np
import matplotlib.pyplot as plt
import save_data
import pandas as pd

path = '.\save_data'
save_path = 'figure'
if not os.path.exists(save_path):
    os.makedirs(save_path)

save_data.delete(save_path)
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

        y_data = [r1[0]]
        count = r1[0]
        for l in range(1, len(r1)):
            count = r1[l] + count
            y_data.append(count)

        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        # fig = plt.figure()
        fig, ax = plt.subplots()

        ax.xaxis.tick_top()
        ax.invert_yaxis()

        # 画水平直方图

        l12 = plt.barh(x, y_data[11], color='#DEB887', alpha=0.8)
        l11 = plt.barh(x, y_data[10], color='#00FFFF', alpha=0.8)
        l10 = plt.barh(x, y_data[9], color='#B8860B', alpha=0.8)
        l9 = plt.barh(x, y_data[8], color='#008B8B', alpha=0.8)
        l8 = plt.barh(x, y_data[7], color='#5F9EA0', alpha=0.8)
        l7 = plt.barh(x, y_data[6], color='#7FFF00', alpha=0.8)
        l6 = plt.barh(x, y_data[5], color='#6495ED', alpha=0.8)
        l5 = plt.barh(x, y_data[4], color='#000000', alpha=0.8)
        l4 = plt.barh(x, y_data[3], color='#FF7F50', alpha=0.8)
        l3 = plt.barh(x, y_data[2], color='#0000FF', alpha=0.8)
        l2 = plt.barh(x, y_data[1], color='#8A2BE2', alpha=0.8)
        l1 = plt.barh(x, y_data[0], color='#DC143C', alpha=0.8)

        # 设置x，y,z轴标签
        ax.set_xlabel(file.replace('.csv', ''))
        ax.set_ylabel('钻孔深度(从浅到深)')

        # 设置注解狂图示
        plt.legend(handles=[l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12],
                   labels=['角闪石', '斜长石', '石英', '云母', '碳酸盐（矿物）', '暗色矿物', '黄铁矿', '黑云母', '石榴子石', '绿帘石', '钠长石', '碳酸盐'],
                   loc='best')
        # 保存和显示

        plt.savefig(save_path + '/' + file.replace('.csv', '.jpg'))
        # plt.show()
