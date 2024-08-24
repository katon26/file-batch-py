import os

def create_files_by_path(path):
    selenium_code = """
#  edit this text
"""
    os.makedirs(path, exist_ok=True)
    for i in range(1, 11):
        filename = os.path.join(path, f"{i}.py")
        with open(filename, 'w') as file:
            file.write(selenium_code)
    print(f"Files created in {path} complete")
