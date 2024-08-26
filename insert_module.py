import os

def insert_strings(file_path, strings, allow_duplicates=False, create=False):
    if not os.path.exists(file_path):
        if create:
            # Create the file if it doesn't exist and the --create flag is used
            with open(file_path, 'w') as f:
                print(f"Created new file: {file_path}")
        else:
            print(f"Error: The file at path '{file_path}' does not exist.")
            return

    print(f"Processing file: {file_path}")
    inserted_lines = 0

    with open(file_path, 'r') as file:
        existing_lines = [line.strip() for line in file.readlines()]

    # Compute new lines to be added
    if not allow_duplicates:
        # Filter out strings that already exist in the file
        new_lines = [s for s in strings if s not in existing_lines]
    else:
        # Allow duplicates, thus all provided strings are considered new lines
        new_lines = strings

    # Write to the file
    with open(file_path, 'a' if allow_duplicates else 'w') as file:
        if not allow_duplicates:
            # Write mode: combine old and new lines and write them out
            all_lines = existing_lines + new_lines
            unique_lines = list(set(all_lines))  # Remove duplicates
            for line in sorted(unique_lines):
                file.write(line + '\n')
            inserted_lines = len(new_lines)  # count of actual new unique entries
        else:
            # Append mode: add all new lines
            for line in new_lines:
                file.write(line + '\n')
                inserted_lines += 1

    print(f"Number of lines inserted: {inserted_lines}")
