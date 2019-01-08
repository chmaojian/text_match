# coding = 'utf-8'
import numpy as np
import xlrd
import xlwt
import pandas as pd
import seaborn as sns
import os
from xlutils.copy import copy
import matplotlib.pyplot as plt


path = 'save_data'
depth_path = 'depth_data'
save_path = 'all_data.csv'
files = os.listdir(path)
file_depth = os.listdir(depth_path)


def read_data():
    # 所有特征值
    feature_all = []
    for file in files:
        if not os.path.isdir(file):
            data_path = path + '/' + file
            data = xlrd.open_workbook(data_path)
            f1 = data.sheet_by_name(u'矿物')
            result = []
            for i in range(1, f1.nrows):
                result.append(f1.row_values(i))
            feature_all.append(result)

    # 所有深度
    depth_all = []
    for file in file_depth:
        if not os.path.isdir(file):
            data_depth = depth_path + '/' + file
            # x_single 是每个钻孔深度数据
            x_single = np.loadtxt(data_depth).tolist()
            depth_all.append(x_single)

    # 将所有深度合并在一起
    dep_data = []
    # 将所有特征合并在一起
    fea_data = []
    for i in range(len(depth_all)):
        if type(depth_all[i]) == list:
            for j in range(len(depth_all[i])):
                dep_data.append(depth_all[i][j])
                fea_data.append(feature_all[i][j])
        if type(depth_all[i]) == float:
            dep_data.append(depth_all[i])
            fea_data.append(feature_all[i][0])

    # 将所有特征转化成 array 形式（508,12），并将深度数据添加进去
    dep_array = np.array(dep_data)
    fea_array = np.array(fea_data)
    data_all = np.c_[dep_array,fea_array].tolist()
    return data_all


def new_excel(save_path, data_all):
    if os.path.exists(save_path):
        os.remove(save_path)
    if not os.path.exists(save_path):
        f = xlwt.Workbook(encoding='utf-8')
        row = [u'深度', u'角闪石', u'斜长石', u'石英', u'云母', u'碳酸盐（矿物）', u'暗色矿物', u'黄铁矿', u'黑云母', u'石榴子石', u'绿帘石', u'钠长石', u'碳酸盐']
        s1 = f.add_sheet(u'钻孔数据', cell_overwrite_ok=True)
        for i in range(len(row)):
            s1.write(0, i, row[i])

        f.save(save_path)

    workbook = xlrd.open_workbook(save_path, formatting_info=True)
    newbook = copy(workbook)
    sheet1 = newbook.get_sheet(0)
    for i in range(len(data_all)):
        for j in range(len(data_all[i])):
            sheet1.write(i+1,j,data_all[i][j])
    newbook.save(save_path)
    return data_all


def draw_1(x_dep,y_feature):
    #分别画出scatter图，但是设置不同的颜色
    plt.scatter(x_dep, y_feature[0] * 0.2, color='#DEB887', label='角闪石', s = 5)
    plt.scatter(x_dep, y_feature[1] * 0.4, color='#00FFFF', label='斜长石', s = 5)
    plt.scatter(x_dep, y_feature[2] * 0.6, color='#B8860B', label='石英', s = 5)
    plt.scatter(x_dep, y_feature[3] * 0.8, color='#008B8B', label='云母', s = 5)
    plt.scatter(x_dep, y_feature[4] * 1.0, color='#5F9EA0', label='碳酸盐（矿物）', s = 5)
    plt.scatter(x_dep, y_feature[5] * 1.2, color='#7FFF00', label='暗色矿物', s = 5)
    plt.scatter(x_dep, y_feature[6] * 1.4, color='#6495ED', label='黄铁矿', s = 5)
    plt.scatter(x_dep, y_feature[7] * 1.6, color='#000000', label='黑云母', s = 5)
    plt.scatter(x_dep, y_feature[8] * 1.8, color='#FF7F50', label='石榴子石', s = 5)
    plt.scatter(x_dep, y_feature[9] * 2.0, color='#0000FF', label='绿帘石', s = 5)
    plt.scatter(x_dep, y_feature[10] * 2.2, color='#8A2BE2', label='钠长石', s = 5)
    plt.scatter(x_dep, y_feature[11] * 2.4, color='#DC143C', label='碳酸盐', s = 5)
    plt.xlabel('钻孔深度')
    plt.ylabel('不同的特征')
    plt.xticks([x for x in range(0,850,50)])
    plt.ylim(ymin=0.1)
    # 设置图例
    plt.legend(loc=(1, 0))
    plt.savefig('scatter_1.jpg')
    #显示图片
    plt.show()


def draw_2(y_feature,x_dep):
    plt.scatter(y_feature[0] * 0.2, x_dep, color='#DEB887', label='角闪石', s = 5)
    plt.scatter(y_feature[1] * 0.4, x_dep, color='#00FFFF', label='斜长石', s = 5)
    plt.scatter(y_feature[2] * 0.6, x_dep, color='#B8860B', label='石英', s = 5)
    plt.scatter(y_feature[3] * 0.8, x_dep, color='#008B8B', label='云母', s = 5)
    plt.scatter(y_feature[4] * 1.0, x_dep, color='#5F9EA0', label='碳酸盐（矿物）', s = 5)
    plt.scatter(y_feature[5] * 1.2, x_dep, color='#7FFF00', label='暗色矿物', s = 5)
    plt.scatter(y_feature[6] * 1.4, x_dep, color='#6495ED', label='黄铁矿', s = 5)
    plt.scatter(y_feature[7] * 1.6, x_dep, color='#000000', label='黑云母', s = 5)
    plt.scatter(y_feature[8] * 1.8, x_dep, color='#FF7F50', label='石榴子石', s = 5)
    plt.scatter(y_feature[9] * 2.0, x_dep, color='#0000FF', label='绿帘石', s = 5)
    plt.scatter(y_feature[10] * 2.2, x_dep, color='#8A2BE2', label='钠长石', s = 5)
    plt.scatter(y_feature[11] * 2.4, x_dep, color='#DC143C', label='碳酸盐', s = 5)
    plt.xlabel('不同的特征')
    plt.ylabel('钻孔深度')
    plt.yticks([x for x in range(0,850,50)])
    plt.xlim(0.1, 2.5)
    plt.xlim(xmin=0.1)

    #设置图例
    plt.legend(loc=(1,0))
    plt.savefig('scatter_2.jpg')
    #显示图片
    plt.show()

# 将所有数据整理在一个表格中
# data_all = read_data()
# data_all = new_excel(save_path,data_all)


# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv('all_data.csv',encoding='utf-8')
x_dep = df['深度']
df_fea_col = ['角闪石', '斜长石', '石英', '云母', '碳酸盐（矿物）', '暗色矿物', '黄铁矿', '黑云母', '石榴子石', '绿帘石', '钠长石', '碳酸盐']
y_feature = []
for i in range(len(df_fea_col)):
    y_feature.append(df[df_fea_col[i]])

draw_1(x_dep,y_feature)
draw_2(y_feature,x_dep)

