from abc import ABC, abstractmethod
import hashlib
import shutil

class DICOMStorageInterface(ABC):
    # Interface that defines the storage operations of dicom files

    @abstractmethod
    def save_file(self, file):
        """ Function to save a dicom file to storage
        @param file: An opened file-like object that contains dicom data

        @output: None - indicates a successful save, else should throw an exception
        """
        raise NotImplementedError

    @abstractmethod
    def query_tag_value(self, hash, tag):
        """ Function to return the tag value corresponding to the input tag
        @param 

        @output: None - indicates a successful save, else throws an exception
        """
        raise NotImplementedError

    @abstractmethod
    def retrieve_file(self, hash):
        """ Function to retrieve a dicom file to storage
        @param hash: A unique hash string that identifies the dicom file

        @output: None - if file not found, else returns a file-like object
        """
        raise NotImplementedError
        

BUF_SIZE = 65536  # read file in 64kb chunks!

def get_hash(file):
    sha1 = hashlib.sha1()
    while True:
        data = file.read(BUF_SIZE)
        if not data:
            break
        sha1.update(data)

    file_hash = "{0}".format(sha1.hexdigest())
    file.seek(0)

    return file_hash

class DICOMLocalStorage(DICOMStorageInterface):
    def __init__(self, path: str):
        self.path = path

    def save_file(self, file):
        dicom_hash = get_hash(file)
        file_path = self.path + dicom_hash
        
        print(file_path)

        with open(file_path, "wb") as f:
            shutil.copyfileobj(file, f)

        return dicom_hash


    def retrieve_file(self, uid):
        pass