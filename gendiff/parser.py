import json
import yaml


def parse(data, file_type):
    if file_type == "yml" or file_type == "yaml":
        return yaml.safe_load(data)
    if file_type == "json":
        return dict(json.load(data))
    raise ValueError(f"Not supported file type - '{file_type}'")
