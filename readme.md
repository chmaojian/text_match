数据：

data_all
文件夹是所有的word原始数据（手动整理得到）

depth_data
所有钻孔的深度数据（手动整理得到）

代码：

save_data.py
匹配实体，并保存在Excel文件中（不用单独执行）

read_word.py
调用save_data.py，从word中读取所有钻孔数据，通过字符串匹配，将匹配结果保存在save_data文件夹中的excel中

show_3d.py
实现多个钻孔放在一张图中的可视化

show_3d_all.py
这个和上面show_3d的功能是一样的，只不过处理方式不一样

show_figures.py
将每个钻孔保存为一张图，保存在figure文件夹中

结果：

save_data文件夹，保存的excel数据

figure文件夹，保存的所有钻孔单独的可视化结果

#   t e x t _ m a t c h 
 
 
