#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:45:27 2021

@author: wyjzll
"""

import nibabel as nib
import numpy as np
import os

inputDir = ""
outputDir = ""

os.chdir(inputDir)

for f in os.listdir():
    # file_name, file_ext = os.path.splitext(f)
    print(f)
    # gender, e, MCN, date, num, T1, m, domes = file_name.split('_')
    # print(e)
    new_name = f[:-12]+ "ori.nii.gz" # in order to delete "domes"
    os.rename(f, new_name)
    print("New name: ", f)
