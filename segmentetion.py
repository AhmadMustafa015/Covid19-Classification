import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pydicom as dicom
import os
import scipy.ndimage
import matplotlib.pyplot as plt

from skimage import measure, morphology, segmentation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Some constants
INPUT_FOLDER = 'covid_dataset/series 2/'
patients = os.listdir(INPUT_FOLDER)
patients.sort()
def rename_dcm(INPUT_FOLDER):
    for filename in os.listdir(INPUT_FOLDER):
            src = INPUT_FOLDER+filename
            dst = INPUT_FOLDER+filename + '.dcm'
            #rename() function will
            #rename all the files
            os.rename(src, dst)
#rename_dcm(INPUT_FOLDER)
import SimpleITK as sitk
from glob import glob
from skimage.util import montage as montage2d
def safe_sitk_read(folder_name, *args, **kwargs):
    """
    Since the default function just looks at images 0 and 1 to determine slice thickness
    and the images are often not correctly alphabetically sorted
    :param folder_name: folder to read
    :return:
    """
    dicom_names = sitk.ImageSeriesReader().GetGDCMSeriesFileNames(folder_name)
    return sitk.ReadImage(dicom_names, *args, **kwargs)
def sitk_to_np(in_img):
    # type: (sitk.Image) -> Tuple[np.ndarray, Tuple[float, float, float]]
    return sitk.GetArrayFromImage(in_img), in_img.GetSpacing()
first_pat = safe_sitk_read(INPUT_FOLDER)
pat_img, pat_spc = sitk_to_np(first_pat)
from lungmask import lungmask
def run():
    segmentation = lungmask.apply(first_pat)
    print('loop')

if __name__ == '__main__':
    run()