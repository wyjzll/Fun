# tensorflow
from keras import backend as K 
def dice_coef(y_true, y_pred, smooth=1):
    """
    Dice = (2*|X & Y|)/ (|X|+ |Y|)
         =  2*sum(|A*B|)/(sum(A^2)+sum(B^2))
    """
    y_true = K.flatten(y_true)
    y_pred = K.flatten(y_pred)
    interp = K.sum(K.abs(y_true * y_pred))
    dice = (2. * interp + smooth) / (K.sum(K.square(y_true)) + K.sum(K.square(y_pred)) + smooth)
    return dice
==============================================================
# Pytorch
import torch 
def dice_coef(pred, target):
    """
    Dice = (2*|X & Y|)/ (|X|+ |Y|)
         =  2*sum(|A*B|)/(sum(A^2)+sum(B^2))
    """
    smooth = 1.
    m1 = pred.view(-1).float()
    m2 = target.view(-1).float()
    interp = (m1 * m2).sum().float()
    dice = (2. * interp + smooth) / (torch.pow(m1, 2).sum() + torch.pow(m2,2).sum() + smooth)
    return dice
==============================================================
#基于numpy实现一个包含全部分割指标的类： 
import numpy as np 
 
class SegMetrics(object):
    def __init__(self, num_class):
        self.num_class = num_class
        self.confusion_matrix = np.zeros((self.num_class,)*2)
 
 
    # 像素准确率
    def Pixel_Accuracy(self):
        Acc = np.diag(self.confusion_matrix).sum() / self.confusion_matrix.sum()
        return Acc
 
 
    # 平均像素准确率
    def Mean_Pixel_Accuracy(self):
        # Precision=TP/(TP+FP)
        Acc = np.diag(self.confusion_matrix) / self.confusion_matrix.sum(axis=1)
        Acc = np.nanmean(Acc)
        return Acc
 
 
    # 平均IoU
    def Mean_IoU(self):
        MIoU = np.diag(self.confusion_matrix) / (
                    np.sum(self.confusion_matrix, axis=1) + np.sum(self.confusion_matrix, axis=0) -
                    np.diag(self.confusion_matrix))
        MIoU = np.nanmean(MIoU)
        return MIoU
 
 
    # 频权IoU
    def Freq_Weighted_IoU(self):
        freq = np.sum(self.confusion_matrix, axis=1) / np.sum(self.confusion_matrix)
        iu = np.diag(self.confusion_matrix) / (np.sum(self.confusion_matrix, axis=1) + np.sum(self.confusion_matrix, axis=0) -
                    np.diag(self.confusion_matrix))
        FWIoU = (freq[freq > 0] * iu[freq > 0]).sum()
        return FWIoU  
 
 
    # Dice系数
    def dice(self):
        dice_coef = 2*np.diag(self.confusion_matrix) / (
            np.sum(self.confusion_matrix, axis=1) + np.sum(self.confusion_matrix, axis=0))
        return dice_coef
 
 
    # 生成混淆矩阵
    def _generate_matrix(self, gt_image, pre_image):
        mask = (gt_image >= 0) & (gt_image < self.num_class)
        label = self.num_class * gt_image[mask] + pre_image[mask]
        count = np.bincount(label, minlength=self.num_class**2)
        confusion_matrix = count.reshape(self.num_class, self.num_class)
        return confusion_matrix
 
 
    # 为真值和预测值生成混淆矩阵
    def add_batch(self, gt_image, pre_image):
        assert gt_image.shape == pre_image.shape
        self.confusion_matrix += self._generate_matrix(gt_image, pre_image)
 
 
    # 重置混淆矩阵
    def reset(self):
        self.confusion_matrix = np.zeros((self.num_class,) * 2)
# ————————————————
# 版权声明：本文为CSDN博主「louwill12」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_37737254/article/details/104337853
