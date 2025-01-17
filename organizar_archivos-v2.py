import os
import shutil
import string

def organize_files_by_letter(directory):
    # Eliminar archivos que contengan el carácter "["
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path) and "[" in item:
            os.remove(item_path)

    # Crear carpetas de la A a la Z
    for letter in string.ascii_uppercase:
        letter_dir = os.path.join(directory, letter)
        if not os.path.exists(letter_dir):
            os.makedirs(letter_dir)

    # Crear carpeta para archivos que no empiezan con letras (opcional)
    others_dir = os.path.join(directory, "Others")
    if not os.path.exists(others_dir):
        os.makedirs(others_dir)

    # Mover archivos a las carpetas correspondientes
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        # Ignorar directorios creados por el script
        if os.path.isdir(item_path):
            continue

        # Determinar la carpeta de destino según la primera letra
        first_char = item[0].upper()
        if first_char in string.ascii_uppercase:
            target_dir = os.path.join(directory, first_char)
        else:
            target_dir = others_dir

        # Mover el archivo
        shutil.move(item_path, os.path.join(target_dir, item))

if __name__ == "__main__":
    target_directory = input("Introduce el directorio donde organizar los archivos: ")
    if os.path.exists(target_directory) and os.path.isdir(target_directory):
        organize_files_by_letter(target_directory)
        print("Archivos organizados correctamente.")
    else:
        print("El directorio especificado no existe o no es válido.")
