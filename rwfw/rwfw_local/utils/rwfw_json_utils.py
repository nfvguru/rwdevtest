import json
import os



def rwfw_create_config(filename, content):
    with open(filename, 'w') as json_file:
        json.dump(content, json_file)
