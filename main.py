import os

def replace_parentheses(filename):
    # Replace '(' with '_'
    new_filename = filename.replace('(', '_')
    return new_filename

def main():
    folder_path = "/home/sam/Downloads/NIE_Master_PDF_Files"

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        # Construct the full path of the file
        full_path = os.path.join(folder_path, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(full_path):
            # Replace parentheses in filename
            new_filename = replace_parentheses(filename)

            # Construct the full path of the new filename
            new_full_path = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(full_path, new_full_path)
            print(f"File '{filename}' renamed to '{new_filename}'.")


if __name__ == "__main__":
    main()