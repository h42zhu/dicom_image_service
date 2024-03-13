from abc import ABC, abstractmethod

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
    def retrieve_file(self, hash: str):
        """ Function to retrieve a dicom file to storage
        @param hash: A unique hash string that identifies the dicom file

        @output: None if file not found, else returns an image as a bytes object
        """
        raise NotImplementedError
        