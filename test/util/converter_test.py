import util.converter
import pytest
import os

def test_dicom_to_array():
    
    # non-existent path raises an error
    with pytest.raises(FileNotFoundError) as _e:
        image_data = util.converter.dicom_to_array("")

    # use one of dicom files saved in the test storage
    hash = "78d0f9c7f2ff47d1af91dacd29ebd66beb7a050e"
    test_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "test_resources", hash)
    image_data = util.converter.dicom_to_array(test_file_path)

    assert len(image_data) > 0