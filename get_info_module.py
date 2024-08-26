import os

def get_file_statistics(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The file at path '{file_path}' does not exist.")
        return
    # Continue with your existing code to process the file
    print(f"Processing file: {file_path}")
    # [Existing file processing logic] ...

    # Use a standard encoding; adjust as needed (e.g., 'utf-8', 'ascii')
    file_encoding = 'utf-8'

    # Analyze the content of the file
    with open(file_path, 'r', encoding=file_encoding) as file:
        lines = [line.strip() for line in file if line.strip()]

    total_lines = len(lines)
    unique_lines = len(set(lines))
    are_duplicates = total_lines > unique_lines

    # Formulate response message
    stats = {
        'Total lines': total_lines,
        'Contains duplicates': are_duplicates
    }
    print(stats)
