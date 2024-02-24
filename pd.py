# print("I am here first")
def set_pd():
    PD_user = int(input("Enter your security parameter: "))

    with open('Files/pd.txt', 'w') as file:
        file.write(str(PD_user))