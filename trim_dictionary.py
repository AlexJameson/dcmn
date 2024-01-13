def remove_duplicates_and_failed_transformations(file_path):
    # Store unique lines
    unique_lines = set()

    # Open the file for reading and writing
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)

        # Write only unique and non-matching lines to the file
        trimmed_lines = 0
        for line in lines:
            if not line.startswith("Failed to") and line not in unique_lines:
                unique_lines.add(line)
                file.write(line)
            else:
                trimmed_lines += 1

        # Truncate any remaining content after the last written line
        file.truncate()

    # Count the resulting number of lines
    resulting_lines = len(unique_lines)

    return trimmed_lines, resulting_lines


if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")

    trimmed, resulting = remove_duplicates_and_failed_transformations(file_path)

    print(f"Number of lines trimmed: {trimmed}")
    print(f"Resulting number of lines: {resulting}")
