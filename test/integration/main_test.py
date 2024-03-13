from fastapi.testclient import TestClient
from fastapi import FastAPI, UploadFile

import os, sys

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.append(os.path.join(parent_dir, "src"))

from main import app

client = TestClient(app)

def test_post_dicom_images():
    test_image = os.path.join("test/integration/test_resources/PA000001/ST000001/SE000001", "IM000001")
    files = {"dicom": ("file", open(test_image, "rb"))}
    response = client.post("/api/v1/dicom_images", files=files)
    
    assert response.status_code == 200
 

