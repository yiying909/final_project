import json
from class_def import Cloth
File_Path = "data.json"

def upload_json(clothes):
    file_names = [cloth.filename for cloth in clothes]
    clothdic = [cloth.__dict__ for cloth in clothes]
    data = {
        "file_names" : file_names,
        "clothdic" : clothdic
    }
    with open(File_Path, "w") as file:
        json.dump(data, file)


def read_json():
    with open(File_Path, 'r') as file:
        data = json.load(file)
    if data:
        filenames = data["file_names"]
        clothdic = data["clothdic"]
        clothes = [Cloth(**cloth) for cloth in clothdic]
        return filenames, clothes
    return [], []