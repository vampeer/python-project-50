from gendiff.cli import gendiff_cli

from gendiff.generate_diff import generate_diff


def main():
    args = gendiff_cli()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == "__main__":
    main()
