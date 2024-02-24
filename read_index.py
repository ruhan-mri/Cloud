import Encryption_files

PD_verify = int(input("Enter your security parameter: "))

with open('Files/pd.txt', 'r') as file:
    for line in file:
        PD_user = int(line)

if(PD_user == PD_verify):
    def read_file_lines(file_path):
        try:
            lines = []
            with open(file_path, 'r') as file:
                for line in file:
                    lines.append(line.strip())
            return lines
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Example usage:
    file_path = 'Files/index.txt'  # Replace 'example.txt' with the path to your file
    lines = read_file_lines(file_path)

    # if lines:
    #     print("File contents (each line as a separate string):")
    #     # print(lines)
    #     for line in lines:
    #         print(len(line))
    #         break

    class IndexClass:
        def __init__(self, ct0, ct1, index):
            self.ct0 = ct0
            self.ct1 = ct1
            self.index = index

    index_object = []
    count_object = int(len(lines)/3)

    for k in range(count_object):
        i = 3 * k

        ct0 = lines[i].split()
        ct0 = list(map(int, ct0)) # convert into int

        ct1 = lines[i+1].split()
        ct1 = list(map(int, ct1))

        index = lines[i+2].split()
        index = list(map(int, index))

        custom_object = IndexClass(ct0, ct1, index)
        index_object.append(custom_object)

    randomized_key = []

    user_input = input("Search your keys : ")
    user_input = user_input.split()
    user_ct = []

    for i in user_input:
        user_ct.append(Encryption_files.key_encryption(i))


    for i in user_ct:
        rk=[]
        for k in range(count_object):
            rk.append(Encryption_files.calculation_func(i, index_object[k].ct0, index_object[k].ct1))
        randomized_key.append(rk)

    # user_zero_check_list = []

    j=0
    for i in randomized_key:
        result = []
        ans = 1
        
        for k in range(count_object):
            # user_zero_check_list.append(Encryption_files.key_decryption(randomized_key[k]))
            ans = Encryption_files.key_decryption(i[k])
            if(ans == 0):
                result = index_object[k].index
                break 
        if(ans):
            print("\nYou search key '{}' doesn't exist.........".format(user_input[j]))
        else:
            print("\nYour file consist of '{}' files list are : {}".format(user_input[j], result))
        
        j+=1
else:
    print("Your security parameter is wrong.. ")
# ------------------ end of code ----------------------------- #