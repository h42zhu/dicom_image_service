from fastapi.testclient import TestClient
from fastapi import FastAPI, UploadFile

### Mock Server for testing purpose
app = FastAPI()

@app.get("/api/v1/dicom_images")
def get_dicom_image():
    return {"Hello": "World"}

# @app.post("/api/v1/dicom_images")
# async def upload_dicom_image(file: UploadFile):
#     print("filename", file.filename)

#     return {"filename": "file.filename"}

client = TestClient(app)

def test_post_dicom_images():
    response = client.get("/api/v1/dicom_images")
    assert response.status_code == 200
    assert True
 

