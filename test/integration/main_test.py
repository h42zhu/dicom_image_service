from fastapi.testclient import TestClient
import os, sys

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(parent_dir, "src"))

# Todo - use dependency injection to test the application where the dicom file storage is different
from main import app

client = TestClient(app)

def test_get_non_existent_dicom_image():
    not_found_response = client.get("/api/v1/dicom_images/123")
    assert not_found_response.status_code == 404

def test_post_invalid_request():
    response = client.post("/api/v1/dicom_images", files=None)
    assert response.status_code == 422

def test_post_and_get_dicom_images():
    test_image = os.path.join("test/integration/test_image/PA000001/ST000001/SE000001", "IM000001")
    files = {"dicom": ("file", open(test_image, "rb"))}
    response = client.post("/api/v1/dicom_images", files=files)
    json = response.json()
    hash = json["identifier"]

    assert response.status_code == 200
    assert type(hash) == str

    # we should be able to get the image that was just stored
    response = client.get("/api/v1/dicom_images/{0}".format(hash))
    assert response.status_code == 200

    image_data = response.content
    assert image_data != ""
    assert type(image_data) == bytes

def test_get_dicom_attributes():
    test_image = os.path.join("test/integration/test_image/PA000001/ST000001/SE000001", "IM000002")
    files = {"dicom": ("file", open(test_image, "rb"))}
    response = client.post("/api/v1/dicom_images", files=files)
    json = response.json()
    hash = json["identifier"]

    # query for some tag of the dicom file we just stored
    response = client.get("/api/v1/dicom_images/{0}/attributes?tag=SOPClassUID".format(hash))
    assert response.status_code == 200
    assert response.json() == {"SOPClassUID": "1.2.840.10008.5.1.4.1.1.4"}

 

