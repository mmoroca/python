import os
import sys

def rename_files_to_lowercase(directory):
    for filename in os.listdir(directory):
        if filename.isupper():
            new_filename = filename.lower()
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else "."  # current directory if no argument is provided
    print("Renaming files in directory", directory)
    rename_files_to_lowercase(directory)
    print("Done!")
