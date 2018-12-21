# coding: utf-8

import numpy as np
import xlrd
import xlwt
from xlutils.copy import copy
import os


def match(str):
    data = xlrd.open_workbook('岩石.xlsx')
    f1 = data.sheet_by_name(u'矿物')
    f2 = data.sheet_by_name(u'侵入岩')
    f3 = data.sheet_by_name(u'蚀变')

    word1 = []
    for i in range(f1.nrows):
        word1.extend(f1.row_values(i))

    feature1 = []
    for i in word1:
        if i in str:
            # feature1.append(i)
            feature1.append(1)
        else:
            feature1.append(0)
    if len(feature1) == 0:
        feature1.append('无')

    word2 = []
    for i in range(f2.nrows):
        word2.extend(f2.row_values(i))

    feature2 = []
    for i in word2:
        if i in str:
            # feature2.append(i)
            feature2.append(1)
        else:
            feature2.append(0)
    if len(feature2) == 0:
        feature2.append('无')

    word3 = []
    for i in range(f3.nrows):
        word3.extend(f3.row_values(i))

    feature3 = []
    for i in word3:
        if i in str:
            # feature3.append(i)
            feature3.append(1)
        else:
            feature3.append(0)
    if len(feature3) == 0:
        feature3.append('无')

    return feature1, feature2, feature3


def delete(path):
    # path = 'save_data'
    files = os.listdir(path)
    for file in files:
        os.remove(path + '/' + file)


def save(f1, f2, f3, path):
    if not os.path.exists(path):
        f = xlwt.Workbook(encoding='utf-8')
        row10 = [u'角闪石', u'斜长石', u'石英', u'云母', u'碳酸盐（矿物）', u'暗色矿物', u'黄铁矿', u'黑云母', u'石榴子石', u'绿帘石', u'钠长石', u'酸盐']
        s1 = f.add_sheet(u'矿物', cell_overwrite_ok=True)
        for i in range(0, len(row10)):
            s1.write(0, i, row10[i])
        row20 = [u'钠长斑岩', u'长英质']
        s2 = f.add_sheet(u'侵入岩', cell_overwrite_ok=True)
        for i in range(0, len(row20)):
            s2.write(0, i, row20[i])
        row30 = [u'钾长石化', u'碳酸盐化', u'硅化', u'绿帘石化', u'黄铁矿化', u'糜棱岩化', u'方铅矿化', u'碎裂岩化']
        s3 = f.add_sheet(u'蚀变', cell_overwrite_ok=True)
        for i in range(0, len(row30)):
            s3.write(0, i, row30[i])
        f.save(path)

    workbook = xlrd.open_workbook(path, formatting_info=True)
    n1 = workbook.sheet_by_name('矿物')
    n2 = workbook.sheet_by_name('侵入岩')
    n3 = workbook.sheet_by_name('蚀变')
    rownum1 = n1.nrows
    rownum2 = n2.nrows
    rownum3 = n3.nrows
    newbook = copy(workbook)
    sheet1 = newbook.get_sheet(0)
    sheet2 = newbook.get_sheet(1)
    sheet3 = newbook.get_sheet(2)
    for j in range(len(f1)):
        sheet1.write(rownum1, j, f1[j])
        newbook.save(path)

    for j in range(len(f2)):
        sheet2.write(rownum2, j, f2[j])
        newbook.save(path)

    for j in range(len(f3)):
        sheet3.write(rownum3, j, f3[j])
        newbook.save(path)
