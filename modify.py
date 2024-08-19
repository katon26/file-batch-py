# !!! if you want to manually add path, use this code !!!
# import os]
#
# def modify_file_by_filename(filename, path=" enter your path here "):

def modify_file_by_filename(filename):
    selenium_code = """
# edit this text
# enter your own anything text or code here 
# to fulfill your file
"""

    # uncomment this code if you want to add path
    # filepath = os.path.join(path, filename)
    
    with open(filename, 'a') as file:
        file.write(selenium_code)
    print(f"File {filename} modified successfully")

# def modify_files_by_range(start, end, path=" enter your path here "):
def modify_files_by_range(start, end):
    selenium_code = """

# edit this text
# enter your own anything text or code here 
# to fulfill your file

"""
    for i in range(start, end + 1):
        # filename = os.path.join(path, f"{i}.py")
        filename = f"{i}.py"
        with open(filename, 'a') as file:
            file.write(selenium_code)
    print(f"Files from {start}.py to {end}.py modified successfully")
