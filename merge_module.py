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


def merge_dictionaries(new_dict, existing_dict):
    
    words_first_file = read_words(new_dict)
    words_second_file = read_words(existing_dict)

    new_words_list = merge_and_sort_words(words_first_file, words_second_file)

    write_words(existing_dict, new_words_list)

