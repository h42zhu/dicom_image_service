import pydicom

def dicom_to_array(dicom_file):
    """ Function to convert from a DICOM image to png
        @param dicom_file: An opened file like object to read te dicom data
        @output An np array representation of the image
    """

    # Extracting data from the dicom file
    dataset = pydicom.dcmread(dicom_file)
    image_2d = dataset.pixel_array

    return image_2d
    
