import os

def change_extension(folder_path, old_ext, new_ext):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(old_ext):
                old_file = os.path.join(root, file)
                new_file = os.path.join(root, file[:-len(old_ext)] + new_ext)
                os.rename(old_file, new_file)
                #print(f'Renamed: {old_file} to {new_file}')

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    old_ext = input("Enter the old extension (including dot): ")
    new_ext = input("Enter the new extension (including dot): ")

    print ('Changing extensions...')
    change_extension(folder_path, old_ext, new_ext)

print ("All Done!")