import pdf
import model
import json
import ai


def save_dict_to_file(dict_obj, file_path):
    with open(file_path, 'w') as file:
        json.dump(dict_obj, file)

def load_dict_from_file(file_path):
    with open(file_path, 'r') as file:
        dict_obj = json.load(file)
        return dict_obj
