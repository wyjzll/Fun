import nibabel as nb
import numpy as np
data = nb.load("/research/Data/ADNI_hdBET/Models_byDavid/statistics/Domes1-5/M__002S0685_20110708073112_401_MT1_m_domes.nii.gz
               ").get_fdata()
print(np.unique(data))
