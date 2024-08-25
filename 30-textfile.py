# 20/8/24
# AIM: To demonstrate the basic operations of reading a text file.

def create_file(_filename):
    """Create a new file or truncate the file if it already exists."""
    with open(_filename, 'w') as _:
        print(f"File '{_filename}' created successfully.")


def write_to_file(_filename):
    print("Enter the text you want to write to the file (type 'EXIT' to stop):")
    with open(_filename, 'a') as file:
        while True:
            line = input()
            if line.strip().upper() == 'EXIT':
                break
            file.write(line + '\n')
    print(f"Text written to '{_filename}' successfully.")


def read_file(_filename):
    """Read and display the contents of the specified file."""

    with open(_filename, 'r') as file:
        content = file.read()
        if content:
            print(f"Contents of '{_filename}':")
            print(content)
        else:
            print(f"File '{_filename}' is empty.")


while True:
    print("\nMenu:")
    print("1. Create a file")
    print("2. Write to a file")
    print("3. Read from a file")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == '1':
        filename = input("Enter the filename to create: ").strip()
        create_file(filename)
    elif choice == '2':
        filename = input("Enter the filename to write to: ").strip()
        write_to_file(filename)
    elif choice == '3':
        filename = input("Enter the filename to read from: ").strip()
        read_file(filename)
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
