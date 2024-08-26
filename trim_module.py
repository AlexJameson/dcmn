import os

def remove_duplicates_and_failed_transformations(file_path, should_sort=False):
    if not os.path.exists(file_path):
        print(f"Error: The file at path '{file_path}' does not exist.")
        return
    # Continue with your existing code to process the file
    print(f"Processing file: {file_path}")
    # [Existing file processing logic] ...

    # Set to store unique lines
    unique_lines = set()

    # Open the file for reading
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if should_sort:
        lines = sorted(lines)

    # Trim lines, remove empty lines and "Failed to" lines, and filter duplicates
    trimmed_lines = 0
    new_lines = []
    for line in lines:
        # Strip whitespace from each line for better empty line detection
        stripped_line = line.strip()
        
        # Skip saving this line if it starts with "Failed to" or if it's empty
        if stripped_line.startswith("Failed to") or not stripped_line:
            trimmed_lines += 1
            continue
        
        # Add unique lines to new_lines for writing back to file
        if stripped_line not in unique_lines:
            unique_lines.add(stripped_line)
            new_lines.append(stripped_line)
        else:
            trimmed_lines += 1

    # Write unique lines back to the file
    with open(file_path, 'w') as file:
        for line in new_lines:
            # Write lines with a newline character
            file.write(line + '\n')

    # Output statistics on the operation
    print(f"Number of lines trimmed (duplicates + errors + empty): {trimmed_lines}")
    print(f"Resulting number of lines (only unique ones): {len(new_lines)}")