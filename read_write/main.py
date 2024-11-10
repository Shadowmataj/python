
#You need to close the file.
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

ABSOLUT_PATH = "/Users/Mata_/OneDrive/Escritorio/my_file.txt"
RELATIVE_PATH = "./../../my_file.txt"

with open(RELATIVE_PATH, mode="w") as file:
    file.write('''Hello, my name is Christian!
I'm 31 years old.
Im' learning python.''')

#You don't need to close the file.
with open(RELATIVE_PATH) as file:
    contents = file.read()
    print(contents)

#Rewrite the entire file
with open(RELATIVE_PATH, mode="w") as file:
    file.write("New text.")

#apend the text at the end of the file.
with open(RELATIVE_PATH, mode="a") as file:
    file.write("\nNew text.")