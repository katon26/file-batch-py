from create import create_files
from modify import modify_file_by_filename, modify_files_by_range
from delete import delete_file

def main_menu():
    while True:
        print("\n=== File Manager Menu ===")
        print("1. Create Files")
        print("2. Modify File by Filename")
        print("3. Modify Files by Range")
        print("4. Delete File")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_files()
            # create_files(path)
        elif choice == '2':
            filename = input("Enter the filename to modify (e.g., 14.py): ")
            modify_file_by_filename(filename)
            # modify_file_by_filename(filename, path)
        elif choice == '3':
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            modify_files_by_range(start, end)
        elif choice == '4':
            filename = input("Enter the filename to delete: ")
            delete_file(filename)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
