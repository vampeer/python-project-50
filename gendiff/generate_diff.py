import os
import json


def merge_keys(first, second):
    merged_keys = [key for key in first.keys()]
    for key in second.keys():
        if key not in merged_keys:
            merged_keys.append(key)
    merged_keys.sort(reverse=False)
    return merged_keys


def generate_diff(first_file, second_file):
    """Get files path and parse json"""
    first = json.load(open(os.path.abspath(first_file)))
    second = json.load(open(os.path.abspath(second_file)))
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
