Created on Mon Mar 29 13:02:13 2021

@author: wyj



import nibabel as nib
import numpy as np
import os

inputDir = "Labels"
outputDir = "Labels2"

if not os.path.exists(outputDir):
    os.makedirs(outputDir)
    
for roots, dirs, files in os.walk(inputDir):
    for file in files:
        print(file)
        data = nib.load(os.path.join(inputDir, file)).get_fdata()
        affine = nib.load(os.path.join(inputDir, file)).affine
        # print(np.unique(data)) 
        data[data == 37] =35
        data[data == 38] =36
        
        for i in range(41, 127):
            data[data == i] = i-4
        # print(np.unique(data))
        save = nib.Nifti1Image(data, affine)
        nib.save(save, os.path.join(outputDir, file))
