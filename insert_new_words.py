# Run by typing python3 insert_new_words.py test_input.txt foo,bar,baz

import argparse

def insert_strings(file_path, strings):
    # Read existing lines from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Append the new strings to the lines list
    lines.extend(strings)

    # Sort the lines alphabetically
    sorted_lines = sorted(lines)

    # Write the sorted lines back to the file
    with open(file_path, 'w') as file:
        for line in sorted_lines:
            file.write(line.rstrip() + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Insert strings into a file while preserving alphabetical order')
    parser.add_argument('file_path', help='Path to the file to write strings into')
    parser.add_argument('strings', nargs='+', help='String or list of comma-separated strings to insert')

    args = parser.parse_args()

    # Remove any whitespace from the string(s) and split into a list of strings
    strings = ''.join(args.strings).split(',')

    insert_strings(args.file_path, strings)