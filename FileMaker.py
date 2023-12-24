import os

print("\n""Crating Username/Password File")


def FileManagment(file_name, data):
    if not os.path.isfile(file_name):
     with open(file_name, "w") as file:
         file.write(data)
         print(f"File '{filename}' Done.""\n")
    else:
        print(f"File 'Filename' Already Exists.""\n")

filename = "Vault.txt"
data = ""

FileManagment(filename, data)
