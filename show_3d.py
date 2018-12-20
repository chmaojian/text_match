from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import os
import xlrd


def show(data_show):
    # data_show 是需要展示的钻孔名称
    # path 是存储所有钻孔数据的总路径
    path = '.\save_data'
    # depth_path 是存储钻孔深度数据的总路径
    depth_path = 'depth_data'

    # result_all 是存储钻孔的特征值
    result_all = []
    for file in data_show:
        if not os.path.isdir(file):
            # data_path 是钻孔的相对路径
            data_path = path + '/' + file + '.csv'
            data = xlrd.open_workbook(data_path)
            f1 = data.sheet_by_name(u'矿物')

            result = []
            for i in range(1, f1.nrows):
                result.append(f1.row_values(i))

            result_all.append(result)

    # 钻孔数量(len(result_all))
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

    # x_data是读取需要显示的钻孔的深度
    x_data = []
    for i in data_show:
        data_depth_all = depth_path + '/' + i + '.txt'
        # x_single 是每个钻孔深度数据
        x_single = np.loadtxt(data_depth_all).tolist()
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
            x = [x_data[j]]
            x_data[j] = x_data[j] / 10

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
    ax.set_title(data_show)

    y_show = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]
    labels = ['角闪石', '斜长石', '石英', '云母', '碳酸盐（矿物）', '暗色矿物', '黄铁矿', '黑云母', '石榴子石', '绿帘石', '钠长石', '碳酸盐']

    print(y_show)

    # # 设置注解图示
    plt.legend(handles=y_show, labels=labels, loc='best')
    plt.show()


if __name__ == '__main__':
    data_list1 = ['8-20老湾ZKE201', '8-21老湾ZKE203']
    show(data_list1)
    data_list2 = ['8-25老湾ZKE1001', '8-26老湾ZKE1002']
    show(data_list2)
    data_list3 = ['8-18老湾ZKW4-1', '8-19老湾ZKW4-2']
    show(data_list3)
    data_list4 = ['8-16老湾ZKW801', '8-17老湾ZKW802']
    show(data_list4)
    data_list5 = ['8-13老湾ZKW1601', '8-14老湾ZKW1602']
    show(data_list5)

