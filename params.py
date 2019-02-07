from os import path
import constant
import uuid

class Param():
    def __init__(self, request):
        self.file_name = request.files["file"].filename.replace(' ', '_')
        print(self.file_name)
        self.file_name_without_ext = path.splitext(self.file_name)[0]
        self.uuid_filename = self.file_name_without_ext + "_" + str(uuid.uuid1())
        self.file_location = path.join(constant.IMAGE_UPLOAD_DIRECTORY, f"{self.uuid_filename}.jpg")
        #file = request["file"]
        #file.save(self.file_location)
