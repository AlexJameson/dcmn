# dcmn: Dictionary Manager utility

## Introduction

This CLI utility is specifically designed to manage dictionaries that aid various linters and spellcheckers for the Russian language. Built using Python 3 and leveraging the `pymorphy3` library, this tool streamlines the process of creating and managing wordlists that are critical to developing and managing language tools.

## Requirements

- `Python 3`
- `pymorphy3`: `pip install pymorphy3`

## Description

`dcmn` offers a toolset for inflecting and conjugating words, and managing dictionaries effectively. It is primarily aimed at assisting developers and content creators in managing dictionaries for programmatically checking text in Russian. Here is a breakdown of what this utility allows:

- **Transformation**: Inflect and conjugate words, managing the linguistic variations that should be recognized by linters or spellcheckers.
- **Insertion of new words**: Add new words to a dictionary file while optionally avoiding duplicates.
- **Trimming**: Remove duplicate entries from a dictionary file to streamline the dictionary size.
- **Getting file info**: Check dictionaries for duplication and length, ensuring dictionary hygiene.
- **Sorting**: Organize dictionary entries in a specified order to improve readability or processing efficiency.

## CLI Command Reference

### transform
  
  `transform <input_file_path> <output_file_path>`
  
  Applies morphological transformation on words from a file at input_file_path and outputs to output_file_path. Words in the source file should be infinitives.

### inflect

  `inflect <words> [--remove-duplicates]`
  
  Generates possible inflections of the provided words and optionally removes duplicates among them. This function accepts words from stdin. The words should be infinitives.

### insert
  
  `insert <file_path> <words> [--allow-duplicates][--create]`
  
  Inserts words into the specified dictionary file and sorts the contents alphabetically. Allows creating a file if it doesn't exist, disabled by default.

### trim

  `trim <file_path> [--sort]`
  
  Removes duplicate words from the dictionary. Can also sort the dictionary if specified.

### get_info

  `get_info <file_path>`
  
  Provides information about the size of the dictionary and checks for duplicates.

### sort

  `sort <file_path>`
  
  Orders the contents of the dictionary alphabetically.

### download_sdd
  
  `download_sdd [--path <download_path>]`
  
  Downloads the latest release of [software-development-dictionary-ru](https://github.com/AlexJameson/software-development-dictionary-ru) from GitHub. Default download path is the current working directory unless specified.
