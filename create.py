def create_files():
    selenium_code = """
    
# edit this text

# anything text or code here

"""

# !!! if you want to manually add path, use this code !!!
# import os
#
# def create_files(path=" enter your path here "):
#     selenium_code = """
# """

    # uncomment this code if you want to add path
    # os.makedirs(path, exist_ok=True)
    
    for i in range(1, 11):
        filename = f"{i}.py"
        with open(filename, 'w') as file:
            file.write(selenium_code)
    print("File creation complete")
