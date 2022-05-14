import json


def make_json_format(dct):
    # with open("diff.json", "w") as infile:
    return json.dumps(dct, indent=4)
