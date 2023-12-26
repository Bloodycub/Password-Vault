import os
import sys

data = ""
filename = "Vault.txt"
print("\nWelcome To Vault")

def FileManagement(file_name):  # Check For File Or Create one.
    if not os.path.isfile(file_name):
        with open(file_name, "w") as file:
            file.write("")
        print(f"File Doesn't Exist, Creating one '{filename}' Done.\n")

def validate(Username, Password):  # Finding Username and Password
    if 5 <= len(Username) <= 16 and 6 <= len(Password) <= 1024:
        try:
            with open(filename, "r") as file:  # Open File
                lines = file.readlines()  # Read All lines
            if f"{Username} : {Password}\n" in lines:  # Find Username and Password
                return True
            else:
                print("No User, Creating one")
                with open(filename, "a") as file:  # Creating New User Based on Input
                    file.write(f"{Username} : {Password}\n")  # Write To File User and Pass
                    print(f"New User: {Username} : {Password}\n")
                return False
        except FileNotFoundError:  # File not found.
            print("No File")
            return False

def FindUsername(Username):
    try:
        with open(filename, "r") as file:
            for line in file:
                if Username in line:
                    return line.strip()
            return "User name not Found"
    except FileNotFoundError:
        print("No File Found")

def get_password():
    while True:
        username = input("User Name: ")
        if 5 <= len(username) <= 16:
            Found = FindUsername(username)
            print(Found)
            print("Thank you for using Vault!")
            print("Good Bye!")
            sys.exit()
        else:
            print("Invalid username length. Please enter a username with a length between 5 and 16 characters.")

def main():
    FindUser = int(input("0 For New Account 1 for Get password. "))
    if FindUser == 1:
        get_password()
    else:
        pass

    print("Enter Username, must be over 5 characters.")
    while True:
        username = input("Enter Username: ")
        if 5 <= len(username) <= 16:
            break
        else:
            print("Invalid username length. Please enter a username with a length between 5 and 16 characters.")

    while True:
        password = input("Enter Password: ")
        if 6 <= len(password) <= 1024:
            break
        else:
            print("Invalid password length. Please enter a password with a length between 6 and 1024 characters.")

    FileManagement(filename)  # Calling Function With FileName.

    if validate(username, password):  # Validate User And Password.
        print("Already Exists\n")

if __name__ == "__main__":
    main()
