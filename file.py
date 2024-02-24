def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return f"File '{filename}' not found."

# Taking file name as input from the user
# filename = input("Enter the name of the file you want to read: ")
filename = 'Files/file1.txt'

# Reading from the file
file_content = read_file(filename)

# Printing the content of the file
print("Content of the file:")
print(file_content)


def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        print("Invalid input. Please enter a valid integer string.")
        return None

def int_to_string(n):
    return str(n)

# Example usage:
s = "ruhan"
integer_value = string_to_int(s)
print("Integer value:", integer_value)

if integer_value is not None:
    string_value = int_to_string(integer_value)
    print("String value:", string_value)






def write_to_file(filename, mode='w'):
    try:
        with open(filename, mode) as file:
            content = input("Enter the content you want to write to the file:\n")
            file.write(content + '\n')
            print("Content has been successfully written to the file.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Taking file name as input from the user
# filename = input("Enter the name of the file you want to write to: ")

# Prompting the user for content to write to the file
write_to_file(filename)  # Writing to the file in write mode

# Asking the user if they want to append more content to the file
while True:
    choice = input("Do you want to append more content to the file? (yes/no): ").lower()
    if choice == 'yes':
        # Appending to the file
        write_to_file(filename, mode='a')
    elif choice == 'no':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
