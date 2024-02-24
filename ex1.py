import math

# Read content from files
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return f"File '{filename}' not found."
    
# Write content to files
def write_to_file(filename, content_list, mode='w'):
    try:
        with open(filename, mode) as file:
            # Convert the list of content string to a space-separated string
            content = ' '.join(map(str, content_list))
            file.write(content + '\n')
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Taking file name as input from the user
# filename = input("Enter the name of the file you want to read: ")
filename = 'Files/file1.txt'
filename2 = 'Files/file2.txt'
filename3 = 'Files/file3.txt'

# Reading from the file
file_content = read_file(filename)

# Character string
char_string = "hello, my name is ruhan"

# Split the sentence into words
words = file_content.split()

# Calculate the length of that array
word_count = len(words)

print("Words array:", words)


integer_array = []

for word in words:
    # print(word)

    # Convert the character string to bytes using UTF-8 encoding
    byte_string = word.encode('utf-8')

    # Convert the byte data to an integer
    integer_value = int.from_bytes(byte_string, byteorder='big')

    # Append the integer value to the list
    integer_array.append(integer_value)

print("Integer array:", integer_array)

# Writing to the file in write mode
write_to_file(filename2, integer_array)

# Reading from the file
file_content = read_file(filename2)

# Split the content into individual integers
file_integer_array = list(map(int, file_content.split()))

word_array = []

for integer_value in file_integer_array:
    # print(integer)

    # Determine the minimum number of bytes needed to represent the integer value
    byte_length = math.ceil(integer_value.bit_length() / 8)
    
    # Convert the integer to byte data with the determined length
    byte_data = integer_value.to_bytes(byte_length, byteorder='big')

    # Convert the byte string back to a character string
    decoded_string = byte_data.decode('utf-8')

    # Append the integer value to the list
    word_array.append(decoded_string)


print("Word array:", word_array)

print("Original sentence:", ' '.join(word_array))

# Writing to the file in write mode
write_to_file(filename3, word_array)