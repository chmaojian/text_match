from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import os
import xlrd


def show(path):
    # path 是需要展示的钻孔文件夹路径,files表示path内的所有钻孔名
    files = os.listdir(path)
    # depth_path 是存储钻孔深度数据的总路径
    depth_path = 'depth_data'
    # result_all 是存储钻孔的特征值
    result_all = []
    for file in files:
        if not os.path.isdir(file):
            data_path = path + '/' + file
            data = xlrd.open_workbook(data_path)
            f1 = data.sheet_by_name(u'矿物')

            result = []
            for i in range(1, f1.nrows):
                result.append(f1.row_values(i))
            result_all.append(result)

    # result_T 是钻孔数据result_all的转置
    result_T = []
    for i in range(len(result_all)):
        single_array = np.array(result_all[i]).T
        result_T.append(single_array)

    fig = plt.figure()
    ax = Axes3D(fig)
    # # 用来正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 特征
    # file_all 存储的是相应的钻孔深度文件名.txt
    file_all = files
    for i in range(len(files)):
        file_all[i] = files[i].replace('csv', 'txt')

    # x_data是读取需要显示的钻孔的深度
    x_data = []
    for i in file_all:
        data_depth = depth_path + '/' + i
        # x_single 是每个钻孔深度数据
        x_single = np.loadtxt(data_depth).tolist()
        x_data.append(x_single)

    for j in range(len(result_T)):
        # y 是第j个钻孔数据
        y = result_T[j]
        # 将深度都缩小十倍,其中x表示深度
        if type(x_data[j]) == list:
            x = x_data[j]
            for t in range(len(x_data[j])):
                x_data[j][t] = x_data[j][t] / 10
        if type(x_data[j]) == float:
            x_data[j] = x_data[j] / 10
            x = [x_data[j]]

        y_data = [y[0]]
        count = y[0]
        for l in range(1, len(y)):
            count = y[l] + count
            y_data.append(count)

        l12 = ax.bar(x, y_data[11], zs=j, zdir='z', color='#DEB887', alpha=0.8)
        l11 = ax.bar(x, y_data[10], zs=j, zdir='z', color='#00FFFF', alpha=0.8)
        l10 = ax.bar(x, y_data[9], zs=j, zdir='z', color='#B8860B', alpha=0.8)
        l9 = ax.bar(x, y_data[8], zs=j, zdir='z', color='#008B8B', alpha=0.8)
        l8 = ax.bar(x, y_data[7], zs=j, zdir='z', color='#5F9EA0', alpha=0.8)
        l7 = ax.bar(x, y_data[6], zs=j, zdir='z', color='#7FFF00', alpha=0.8)
        l6 = ax.bar(x, y_data[5], zs=j, zdir='z', color='#6495ED', alpha=0.8)
        l5 = ax.bar(x, y_data[4], zs=j, zdir='z', color='#000000', alpha=0.8)
        l4 = ax.bar(x, y_data[3], zs=j, zdir='z', color='#FF7F50', alpha=0.8)
        l3 = ax.bar(x, y_data[2], zs=j, zdir='z', color='#0000FF', alpha=0.8)
        l2 = ax.bar(x, y_data[1], zs=j, zdir='z', color='#8A2BE2', alpha=0.8)
        l1 = ax.bar(x, y_data[0], zs=j, zdir='z', color='#DC143C', alpha=0.8)

    ax.set_xlabel('Z/深度*10m')
    ax.set_ylabel('X/特征')
    ax.set_zlabel('Y/钻孔')
    ax.set_title(path)
    y_show = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    labels = ['角闪石', '斜长石', '石英', '云母', '碳酸盐（矿物）', '暗色矿物', '黄铁矿', '黑云母', '石榴子石', '绿帘石', '钠长石', '碳酸盐']

    # # 设置注解图示
    plt.legend(handles=y_show, labels=labels, loc='best')

    plt.show()


if __name__ == '__main__':
    # path = './save_data'
    # show(path)
    # path1 = 'ZKE1001ZKE1002'
    # show(path1)
    path2 = 'ZKE201ZKE203'
    show(path2)
    # path3 = 'ZKW4_1ZKW4_2'
    # show(path3)
    # path4 = 'ZKW801ZKW802'
    # show(path4)
    # path5 = 'ZKW1601ZKW1602'





