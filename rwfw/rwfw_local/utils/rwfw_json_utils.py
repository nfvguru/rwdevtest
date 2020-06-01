import json
import os



def rwfw_create_config(filename, content):
    with open(filename, 'w') as json_file:
        json.dump(content, json_file)


def rwfw_get_img_from_config(config_file):
    with open(config_file.name) as f:
        f_db = json.load(f)
        c_db = f_db['rwfw_img']
        img_name = c_db['img']
        return img_name
