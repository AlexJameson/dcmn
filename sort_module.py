import os

def sort_file_contents(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The file at path '{file_path}' does not exist.")
        return
    # Continue with your existing code to process the file
    print(f"Processing file: {file_path}")

    file_encoding = 'utf-8'
    
    # Read and process the content of the file
    with open(file_path, 'r', encoding=file_encoding) as file:
        lines = [line.strip() for line in file if line.strip()]

    total_lines = len(lines)
    unique_lines = len(set(lines))
    are_duplicates = total_lines > unique_lines

    # Sorting the lines
    sorted_lines = sorted(lines)

    # Writing the sorted content back to the file
    with open(file_path, 'w', encoding=file_encoding) as file:
        for line in sorted_lines:
            file.write(line + '\n')

    # Reporting the results
    print(f"File '{file_path}' has been sorted. Number of lines: {total_lines}.")
    if are_duplicates:
        print("Duplicates were found in the file.")
    else:
        print("No duplicates were found in the file.")

