import nibabel as nb
import numpy as np
data = nb.load("/****/**.nii.gz
               ").get_fdata()
print(np.unique(data))
