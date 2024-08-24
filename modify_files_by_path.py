import os

def modify_file_by_filename_in_path(filename, path):
    selenium_code = """
# edit this text
"""
    filepath = os.path.join(path, filename)
    with open(filepath, 'a') as file:
        file.write(selenium_code)
    print(f"File {filename} modified successfully in {path}")

def modify_files_by_range_in_path(start, end, path):
    selenium_code = """
# anything text or code here
"""
    for i in range(start, end + 1):
        filename = os.path.join(path, f"{i}.py")
        with open(filename, 'a') as file:
            file.write(selenium_code)
    print(f"Files from {start}.py to {end}.py modified successfully in {path}")
