from PIL import Image
import hashlib
import shutil
import os.path
import util.converter
import pydicom
import ports.dicom


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

class DICOMLocalStorage(ports.dicom.DICOMStorageInterface):
    def __init__(self, path: str):
        self.path = path

    def save_file(self, file):
        dicom_hash = get_hash(file)
        file_path = os.path.join(self.path, dicom_hash)
        print("saving file to: ", file_path)
        
        if os.path.exists(file_path):
            # noop if the file already exists
            return dicom_hash

        with open(file_path, "wb") as f:
            shutil.copyfileobj(file, f)

        return dicom_hash

    def retrieve_file(self, hash: str):
        file_path = os.path.join(self.path, hash)

        if os.path.exists(file_path):
            image_2d = util.converter.dicom_to_array(file_path)
            
            im = Image.fromarray(image_2d)

            # Uncomment lines below to enable save image as png to disk
            # png_path = os.path.join(self.path, hash + ".png")
            # cv2.imwrite(png_path, image_2d)

            return im.tobytes()
        else:
            raise FileNotFoundError()

    def query_tag_value(self, hash, tag):
        file_path = os.path.join(self.path, hash)

        if not os.path.exists(file_path):
            raise FileNotFoundError()
        
        dataset = pydicom.dcmread(file_path, force=True)
        element = dataset[tag]

        if element is None:
            return {}

        return {element.keyword: element.value}