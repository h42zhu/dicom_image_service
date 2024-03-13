## Overview

A Python FASTAPI based microservice that supports the following functionalities:

- Post DICOM Files to be stored
- Retrieve DICOM Files as PNG images, each stored dicom file is identified by an unique hash key
- Retrieve DICOM Attributes values based on [DICOM tags](https://www.dicomlibrary.com/dicom/dicom-tags/)


## Getting Started

Running this service locally requires Python 3.8+ and uvicorn and other python dependencies

TODO: Add a dockerfile to allow running this service with Docker


### Running the HTTP server locally

Use the following command to run this service locally:

```
cd src && uvicorn main:app
```

## API Docs

Once the server is running locally, go to `http://127.0.0.1:8000/docs`

One will see the automatic interactive API documentation

Alternatively, go to `http://127.0.0.1:8000/redoc` for the redoc powered documenation

### Running Tests

This repo uses `pytest` for testing

Run the `pytest` command will invoke all the tests which includes unit tests as well as integration tests

## Architecture

The code is mostly organized using the [hexagonal architecture](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)) pattern

The `resources` folder is used for storing the dicom files. In future iterations, the storage adapter can be swapped out to use a blob storage solution, such as S3, instead of storing files locally

The `test_resources` folder is used for storing the dicom files when running the unit tests
