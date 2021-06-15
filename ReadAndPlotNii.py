import numpy as np
import os
import glob
import SimpleITK as sitk
from scipy import ndimage
import matplotlib.pyplot as plt

# LiST数据集为例，data是volume，lable是segmementation，nii格式
# 加r，可以将路径转换为原始字符串，不用变为‘\\’ 
data_path = r'/research/Data/ADNI100_HDBET_WYJ_test/git/3DUNet-Pytorch-master/ADNi/fixed_lits/ct'
label_path = r'/research/Data/ADNI100_HDBET_WYJ_test/git/3DUNet-Pytorch-master/ADNi/fixed_lits/label'

dataname_list = os.listdir(data_path)
dataname_list.sort()
ori_data = sitk.ReadImage(os.path.join(data_path, dataname_list[2]))  # 读取一个数据
data1 = sitk.GetArrayFromImage(ori_data)  # 获取数据的array



print(dataname_list[2], data1.shape, data1[175,125,65])  #打印数据name、shape、某一个位置的元素的值（z,y,x）

for i in range(199):
    plt.imshow(data1[i,:,:]) # 对第100张slice可视化
    plt.show()
