import json


def load_properties_file_data(file_path):
    """
    This will load and return properties file data as dictionary
    :param file_path:
    :return:
    """
    env_data = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.rstrip()
            if "=" not in line: continue
            if line.startswith("#"): continue
            k, v = line.split("=", 1)
            env_data[k] = v
    return env_data


def load_json_file_data(file_path):
    """
    This will load and return json file data dictionary
    :param file_path:
    :return:
    """
    with open(file_path, "rb") as f:
        return json.load(f)
