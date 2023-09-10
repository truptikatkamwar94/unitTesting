import json


def save_dict(_dict,filepath):
    json.dump(_dict,open(filepath,'w'))#saving dictionary as a json obj in a given path
    print("saved")