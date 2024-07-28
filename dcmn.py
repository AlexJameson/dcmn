#!/usr/bin/env python3
import argparse
import sys
from insert_module import insert_strings
from process_and_transform_module import process_and_transform
from trim_module import remove_duplicates_and_failed_transformations

def main():
    parser = argparse.ArgumentParser(prog="dcmn", description="Utility to manage vocabularies.")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    parser_insert = subparsers.add_parser('insert', help='Insert new words into a file.')
    parser_insert.add_argument('file_path', type=str, help='The file where strings will be inserted.')
    parser_insert.add_argument('strings', nargs='+', help='Words to insert.')
    parser_insert.add_argument('--search-duplicates', action='store_true', help='Ignore duplicate words.')
    
    parser_transform = subparsers.add_parser('transform', help='Inflect and conjugate words from a file.')
    parser_transform.add_argument('input_file_path', type=str, help='The file from which to get strings.')
    parser_transform.add_argument('output_file_path', type=str, help='The file from where to insert processed and transformed strings.')

    parser_trim = subparsers.add_parser('trim', help='Remove duplicates from a file.')
    parser_trim.add_argument('file_path', type=str, help='The file where strings will be inserted.')

    args = parser.parse_args()

    if args.command == 'insert':
        insert_strings(args.file_path, args.strings, args.search_duplicates)
    if args.command == 'transform':
        process_and_transform(args.input_file_path, args.output_file_path)
    if args.command == 'trim':
        remove_duplicates_and_failed_transformations(args.file_path)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()