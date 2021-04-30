""" Read nii mask and save to .csv """ 
import nibabel as nib
import numpy as np
import os
import pandas as pd
import glob

inputDir = ""
outputDir = ""

# ####################### Check classes in all the domes files and converted to .csv one by one
# if not os.path.exists(outputDir):
#    os.makedirs(outputDir)
    
#for roots, dirs, files in os.walk(inputDir):
    
#    for file in files:
        
#        print(file)
#        data = nib.load(os.path.join(inputDir, file)).get_fdata()
#        affine = nib.load(os.path.join(inputDir, file)).affine
        # np.set_printoptions(threshold=np.inf)
        # print(data)
        # classes_array = np.unique(data)
        # classes_array = np.append(classes_array)
#        np.savetxt(os.path.join(outputDir, file)+".csv", np.unique(data))
        
        # print(affine)
        # print(np.unique(data))
        # classes_array = np.append(data,np.unique(data),axis=0)
        
# ########################Conbine all the .csv to one file (.csv ) 

os.chdir('/research/Data/ADNI_hdBET/Models_byDavid/statistics/CsvForAllLabels4')
file_extension = '.csv'
all_filenames = [i for i in glob.glob(f"*{file_extension}")]
print(f"These are all of the filenames ending in .csv {all_filenames}.")
combined_csv_data = pd.concat([pd.read_csv(f, delimiter='t', encoding='UTF-8') for f in all_filenames])
os.chdir("..")
combined_csv_data.to_csv('combined_Csvlabel4.csv') 
