import os

def delete_file_in_path(filename, path):
    filepath = os.path.join(path, filename)
    try:
        os.remove(filepath)
        print(f"File {filename} deleted successfully from {path}")
    except FileNotFoundError:
        print(f"File {filename} not found in {path}")
