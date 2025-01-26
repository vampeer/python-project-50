import argparse


def gendiff_cli():
    parser = argparse.ArgumentParser(
        usage="usage: gendiff [-h] [-f FORMAT] first_file second_file",
        description="Compares two configuration files and shows a difference.",
    )

    parser.add_argument("first_file")
    parser.add_argument("second_file")

    parser.add_argument("-f", "--format", help="set format of output")

    args = parser.parse_args()
    return args
