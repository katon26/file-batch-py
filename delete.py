import os

# !!! if you want to manually add path, use this code !!!
# def delete_files(path=" enter your path here "):

def delete_file(filename):
    # filepath = os.path.join(path, filename)
    try:
        # os.remove(filepath)
        os.remove(filename)
        print(f"File {filename} deleted successfully")
    except FileNotFoundError:
        print(f"File {filename} not found")
