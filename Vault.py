import os


print("\nWelcome To Vault")
print("Login")
print("Enter Username Must be over 5 Characters")
print("Pass")

data = ""
filename = ("Vault.txt")
while True:
    username = input("Enter Username: ")
    if 5 <= len(username) <= 16:
        break
    else:
        print("Invalid username length. Please enter a username with length between 5 and 16 characters.")

while True:
    password = input("Enter Password: ")
    if 6 <= len(password) <= 1024:
        break
    else:
        print("Invalid password length. Please enter a password with length between 6 and 1024 characters.")

def FileManagment(file_name):
    if not os.path.isfile(file_name):
     with open(file_name, "w") as file:
         file.write("")
         print(f"File Dosent Exist Crating one '{filename}' Done.""\n")

FileManagment(filename)

def validate(Username,Password):
    if 5 <= len(Username) <=16 and 6<=len(Password) <=1024:
        try:
            with open(filename, "r") as file:
                lines = file.readlines()

            if f"{Username}:{Password}\n" in lines:
                return True
            else:
                print("No User Crating one")
                with open(filename, "a") as file:
                    file.write(f"{Username}:{Password}\n")
                    print(f"New User: {Username}:{Password}\n")
                return False

        except FileNotFoundError:
            print("No File")
            return False

if validate(username,password):
    print("Found\n")








