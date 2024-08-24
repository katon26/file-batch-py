from create import create_files
from modify import modify_file_by_filename, modify_files_by_range
from delete import delete_file

from create_files_by_path import create_files_by_path
from modify_files_by_path import modify_file_by_filename_in_path, modify_files_by_range_in_path
from delete_files_by_path import delete_file_in_path

def main_menu():
    while True:
        print("\n=== File Manager Menu ===")
        print("1. Create Files")
        print("2. Modify File by Filename")
        print("3. Modify Files by Range")
        print("4. Delete File")
        print("5. Create Files by Path")
        print("6. Modify File by Filename in Path")
        print("7. Modify Files by Range in Path")
        print("8. Delete File in Path")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            create_files()
        elif choice == '2':
            filename = input("Enter the filename to modify (e.g., 14.py): ")
            modify_file_by_filename(filename)
        elif choice == '3':
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            modify_files_by_range(start, end)
        elif choice == '4':
            filename = input("Enter the filename to delete: ")
            delete_file(filename)
        elif choice == '5':
            path = input("Enter the path where files will be created: ")
            create_files_by_path(path)
        elif choice == '6':
            path = input("Enter the path where the file is located: ")
            filename = input("Enter the filename to modify (e.g., 14.py): ")
            modify_file_by_filename_in_path(filename, path)
        elif choice == '7':
            path = input("Enter the path where the files are located: ")
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            modify_files_by_range_in_path(start, end, path)
        elif choice == '8':
            path = input("Enter the path where the file is located: ")
            filename = input("Enter the filename to delete: ")
            delete_file_in_path(filename, path)
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
