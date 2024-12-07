import json
from core.class_def import Cloth
File_Path = "data.json"

def upload_json(clothes, pre_filenames, pre_clothes):
    pre_clothesdic = [cloth.__dict__ for cloth in pre_clothes]
    file_names = [cloth.filename for cloth in clothes]
    clothdic = [cloth.__dict__ for cloth in clothes]
    update_filenames = pre_filenames + file_names
    update_clothes = pre_clothesdic + clothdic
    data = {
        "filenames" : update_filenames,
        "clothdic" : update_clothes
    }
    with open(File_Path, "w") as file:
        json.dump(data, file, indent=4)
    return update_filenames


def read_json():
    with open(File_Path, 'r') as file:
        data = json.load(file)
    if data:
        filenames = data["filenames"]
        clothdic = data["clothdic"]
        clothes = [Cloth(**cloth) for cloth in clothdic]
        return filenames, clothes
    return [], []