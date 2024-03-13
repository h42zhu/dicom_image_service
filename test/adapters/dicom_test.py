import os, sys
import pytest

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.append(os.path.join(parent_dir, "src"))
import adapters.dicom as dicom

test_resources_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "test_resources")
dicom_storage = dicom.DICOMLocalStorage(test_resources_dir)

def test_dicom_storage_save_file():

    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "integration", "test_image", "PA000001", "ST000001", "SE000001", "IM000004")

    with open(file_path, "rb") as f:
        hash = dicom_storage.save_file(f)


    assert type(hash) == str
    assert hash != ""

def test_dicom_storage_retrieve_file():
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "integration", "test_image", "PA000001", "ST000001", "SE000001", "IM000002")

    hash = ""
    with open(file_path, "rb") as f:
        hash = dicom_storage.save_file(f)

    image_data = dicom_storage.retrieve_file(hash)

    assert type(image_data) == bytes
    assert len(image_data) > 0

    # retrieve non-existent file raises FileNotFoundError
    with pytest.raises(FileNotFoundError) as _e:
        image_data = dicom_storage.retrieve_file("abcd")


def test_dicom_query_tag_value():
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "integration", "test_image", "PA000001", "ST000001", "SE000001", "IM000003")

    hash = ""
    with open(file_path, "rb") as f:
        hash = dicom_storage.save_file(f)

    result = dicom_storage.query_tag_value(hash, "PatientName")
    assert result == {'PatientName': 'NAYYAR^HARSH'}

    # retrieve non-existent file raises FileNotFoundError
    with pytest.raises(FileNotFoundError) as _e:
        result = dicom_storage.query_tag_value("abcd", "PatientName")

    # retrieve non-existent tag raises KeyError
    with pytest.raises(KeyError) as _e:
        result = dicom_storage.query_tag_value(hash, "foobar")