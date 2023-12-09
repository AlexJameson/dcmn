# 1. Reads words from the first file using the read_words function.
# 2. Reads words from the second (alphabetically sorted) file using the read_words function.
# 3. Merges both word lists, removes duplicates, and sorts the combined list in alphabetical order using the merge_and_sort_words function.
# 4. Writes the sorted word list back to the second file using the write_words function.

def read_words(file_path):
    with open(file_path, 'r') as file:
        words = [word.strip() for word in file.readlines()]
    return words


def write_words(file_path, words):
    with open(file_path, 'w') as file:
        file.writelines([word + '\n' for word in words])


def merge_and_sort_words(words1, words2):
    merged_words = sorted(set(words1 + words2))
    return merged_words


def main():
    file_path1 = 'words_first_file.txt'
    file_path2 = 'words_second_file.txt'
    
    words_first_file = read_words(file_path1)
    words_second_file = read_words(file_path2)

    new_words_list = merge_and_sort_words(words_first_file, words_second_file)

    write_words(file_path2, new_words_list)


if __name__ == "__main__":
    main()
