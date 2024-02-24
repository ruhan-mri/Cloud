import pd
import Encryption_files
import os

pd.set_pd()

index = {}
char_count=[-9999]  


def add_in_dictionary(sentence,num):
    words = sentence.split()
    for i in words:
        if i in index:
            if(num in index[i]):
                continue
            index[i].append(num)
        else:
            index[i]=[num]

def key_enc(key):
    ct = Encryption_files.key_encryption(key)
    x0 = ct[0].F
    x1 = ct[1].F
    content1 = ' '.join(map(str, x0))
    content2 = ' '.join(map(str, x1))
    return content1,content2

def add_prove_msg():
    for key in index:
        sum = 0
        for i in index[key]:
           sum+=char_count[i]
        index[key].append(sum)

# Creating index
for i in range(1, 11):  # Assuming file names are file1, file2, ..., file10
    file_name = f"Files/file{i}.txt"  # Construct the file name
    try:
        with open(file_name, "r") as file:
            # Read the contents of the file
            content = file.read()
            content= content.lower()
            char_count.append(len(content))
            add_in_dictionary(content,i)
            file.close()
    except FileNotFoundError:
        print(f"File {file_name} not found.")

add_prove_msg()

def write_to_file(filename, mode='a'):
    #creating index file with encryption
    try:
        with open(filename, mode) as file:
            for key in index:
                c0, c1 = key_enc(key)
                file.write(c0)
                file.write("\n")
                file.write(c1)
                file.write("\n")
                for i in index[key]:
                    file.write(str(i)+" ")
                file.write("\n")
            file.close()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

filename4 = 'Files/index.txt'
if os.path.exists(filename4):
    # If the file exists, delete it
    os.remove(filename4)
write_to_file(filename4)