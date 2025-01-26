import os
import json
import yaml
from yaml import Loader


def is_yaml(filename):
    if not (filename.find(".yaml") == -1) or not (filename.find(".yml") == -1):
        return True
    return False


def is_json(filename):
    if not (filename.find(".json") == -1):
        return True
    return False


def parse_file(filepath):
    if is_yaml(filepath):
        return yaml.load(open(os.path.abspath(filepath)), Loader=Loader)
    if is_json(filepath):
        return json.load(open(os.path.abspath(filepath)))


def merge_keys(first, second):
    merged_keys = [key for key in first.keys()]
    for key in second.keys():
        if key not in merged_keys:
            merged_keys.append(key)
    merged_keys.sort(reverse=False)
    return merged_keys


def generate_diff(first_file, second_file):
    """Get files path and parse json"""
    first, second = parse_file(first_file), parse_file(second_file)
    print(first)
    """Merge both dictionary keys and sort them"""
    merged_keys = merge_keys(first, second)

    diff = {}
    for item in merged_keys:
        if (item in first.keys()) and (item in second.keys()):
            if first[item] == second[item]:
                diff["  " + item] = first[item]
                continue
            else:
                diff["- " + item] = first[item]
                diff["+ " + item] = second[item]
                continue
        if item in first.keys():
            diff["- " + item] = first[item]

        if item in second.keys():
            diff["+ " + item] = second[item]

    result = "{\n"
    for key, value in diff.items():
        result += "  " + str(key) + ": " + str(value) + "\n"
    result += "}"
    return result.lower()
