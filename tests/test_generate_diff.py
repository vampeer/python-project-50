import os
import json

from gendiff import generate_diff


def get_case_file(filename):
    f = open(os.path.abspath("tests/test_data/" + filename), "r")
    return f.read()


def test_both_empty():
    assert generate_diff(
        "tests/test_data/empty.json", "tests/test_data/empty.json"
    ) == get_case_file("empty.txt")


def test_exercise():
    assert generate_diff(
        "tests/test_data/file1.json", "tests/test_data/file2.json"
    ) == get_case_file("exercise_case.txt")


# for filename in cases.keys():
# os.remove(filename + ".json")
