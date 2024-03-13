"""
An HTTP service using the FastAPI library

The service exposes three routes:

POST api/v1/dicom_images/
GET api/v1/dicom_images/:id
GET api/v1/dicom_images/:id/attributes?tag={tags}

The first route allows the caller to upload a dicom image to the this service to be stored
Responds with a hash string for the image resource if the operation is successful

The second route allows the caller to retrieve a dicom image based on a hash string,
Responds with a PNG file to be displayed

The third route allows the caller to query a dicom image based on an a hash string and tags
Responds with a JSON that contains the value of the queried tags
"""

import adapters.dicom
import os

from fastapi import FastAPI, UploadFile
from starlette.responses import Response

dicom_storage = adapters.dicom.DICOMLocalStorage(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "resources"))
app = FastAPI()

@app.get("/api/v1/dicom_images/{hash}",
        responses = {
            200: {"content": {"image/png": {}}}
        },
        response_class=Response
)
def get_dicom_image(hash: str):
    try:
        image = dicom_storage.retrieve_file(hash)
        return Response(content=image, media_type="image/png")
    except FileNotFoundError:
        return Response("File not found", status_code=404)
    
@app.get("/api/v1/dicom_images/{hash}/attributes")
def get_dicom_attributes(hash: str, tag: str):
    try:
        result = dicom_storage.query_tag_value(hash, tag)
        return result
    except FileNotFoundError:
        return Response("File not found", status_code=404)

@app.post("/api/v1/dicom_images")
async def upload_dicom_image(dicom: UploadFile):
    try:
        print("storing file...")
        hash = dicom_storage.save_file(dicom.file)
        return {"identifier": hash}
    except Exception:
        return Response("Internal server error", status_code=500)

