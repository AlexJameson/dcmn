#!/usr/bin/env python3
import argparse
from insert_module import insert_strings
from process_and_transform_module import process_and_transform
from trim_module import remove_duplicates_and_failed_transformations
from transform_single_module import process_word
from get_info_module import get_file_statistics
from sort_module import sort_file_contents
from download_sdd_module import download_latest_release

def main():
    parser = argparse.ArgumentParser(prog="dcmn", description="Utility to manage dictionaries.")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    parser_insert = subparsers.add_parser('insert', help='Insert new words into a file.')
    parser_insert.add_argument('file_path', type=str, help='The file where strings will be inserted.')
    parser_insert.add_argument('strings', nargs='+', help='Words to insert.')
    parser_insert.add_argument('--allow-duplicates', action='store_true', help='Allow inserting duplicates. Disabled by default')
    parser_insert.add_argument('--create', action='store_true', help='Create a file if it does not exist')
    
    parser_transform = subparsers.add_parser('transform', help='Inflect and conjugate words from a file.')
    parser_transform.add_argument('input_file_path', type=str, help='The file from which to get strings.')
    parser_transform.add_argument('output_file_path', type=str, help='The file where to insert processed and transformed strings.')

    parser_trim = subparsers.add_parser('trim', help='Remove duplicates from a file.')
    parser_trim.add_argument('file_path', type=str, help='The file where strings will be inserted.')
    parser_trim.add_argument('--sort', action='store_true', help='Sort file content. Disabled by default')

    parser_inflect = subparsers.add_parser('inflect', help='Inflect words into possible forms.')
    parser_inflect.add_argument('words', type=str, nargs='+', help='Words to inflect.')

    parser_inflect.add_argument('--remove-duplicates', action='store_true', help='Remove duplicate inflections.')

    parser_check = subparsers.add_parser('get_info', help='Get the number of lines and check for duplicates.')
    parser_check.add_argument('file_path', type=str, help='The file to check.')
    
    parser_sort = subparsers.add_parser('sort', help='Sort file contents.')
    parser_sort.add_argument('file_path', type=str, help='The file whose contents to sort.')
    
    parser_sdd = subparsers.add_parser('download_sdd', help='Download the latest software-development-dictionary-ru release from GitHub.')
    parser_sdd.add_argument('--path', type=str, default=None,
                        help='Optional. Destination path for the downloaded file. Defaults to current working directory.')

    args = parser.parse_args()

    if args.command == 'insert':
        insert_strings(args.file_path, args.strings, args.allow_duplicates, args.create)
    if args.command == 'transform':
        process_and_transform(args.input_file_path, args.output_file_path)
    if args.command == 'trim':
        remove_duplicates_and_failed_transformations(args.file_path, args.sort)
    if args.command == 'get_info':
        get_file_statistics(args.file_path)
    if args.command == 'sort':
        sort_file_contents(args.file_path)
    if args.command == 'download_sdd':
        download_latest_release(args.path)
    if args.command == 'inflect':
        for word in args.words:
            results = process_word(word, args.remove_duplicates)
            print(f"Inflections for '{word}':")
            for result in results:
                print(result)
            print()

if __name__ == '__main__':
    main()