import os
import sys

def rename_files_to_lowercase(directory):
    for filename in os.listdir(directory):
        if filename.isupper():
            new_filename = filename.lower()
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else "."  # si no se pasa directorio toma el actual
    print("Renombrando archivos en el directorio", directory)
    rename_files_to_lowercase(directory)
    print("Hecho.")
