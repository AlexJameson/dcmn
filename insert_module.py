def insert_strings(file_path, strings, search_duplicates=False):
    with open(file_path, 'r') as file:
        existing_lines = [line.strip() for line in file]

    if search_duplicates:
        # Filter out strings that already exist in the file
        strings = [s for s in strings if s not in existing_lines]

    # Combine old and new lines, sort, and remove duplicates if not checking explicitly
    updated_lines = sorted(set(existing_lines + strings))

    with open(file_path, 'w') as file:
        for line in updated_lines:
            file.write(line + '\n')