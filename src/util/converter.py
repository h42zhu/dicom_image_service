import os
import pydicom
import numpy as np
import sys

def dicom_to_png(dicom_file, png_file):
    """ Function to convert from a DICOM image to png

        @param mri_file: An opened file like object to read te dicom data
        @param png_file: An opened file like object to write the png data
    """

    # Extracting data from the mri file
    plan = pydicom.read_file(dicom_file)
    shape = plan.pixel_array.shape

    #Convert to float to avoid overflow or underflow losses.
    image_2d = plan.pixel_array.astype(float)
    image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max())

    np.save(png_file, image_2d_scaled.astype(np.float16))


def convert_to_png_file(dicom_file_path, png_file_path):
    """ Function to convert an MRI binary file to a
        PNG image file.

        @param dicom_file_path: Full path to the dicom file
        @param png_file_path: Fill path to the png file
    """

    # Making sure that the mri file exists
    if not os.path.exists(dicom_file_path):
        raise Exception('File "%s" does not exists' % dicom_file_path)

    with open(dicom_file_path, 'rb') as dicom:

        dicom_to_png(dicom_file_path, png_file)
