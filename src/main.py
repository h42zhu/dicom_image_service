"""
An HTTP Server using the FastAPI library

The server handles three routes:

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

import pydicom
import os
import sys

import adapters.dicom

from fastapi import FastAPI, UploadFile
from starlette.responses import Response

dicom_storage = adapters.dicom.DICOMLocalStorage(f"../resources/")
app = FastAPI()

@app.get("/api/v1/dicom_images/{hash}")
def get_dicom_image(hash: str):

    retrieve_file_metadata(file_path)

    return {"Hello": "World"}

@app.post("/api/v1/dicom_images")
async def upload_dicom_image(dicom: UploadFile):
    try:
        hash = dicom_storage.save_file(dicom.file)
        return {"identifier": hash}
    except Exception:
        return Response("Internal server error", status_code=500)

    
def retrieve_file_metadata(file_path):
    print("retrieve_file_metadata")
    dataset = pydicom.dcmread(file_path)
    print(dataset)

