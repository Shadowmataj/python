#TRY: something that might cause an exception
#EXCEPT: do this fi there was an exception
#ELSE: do this if there were no exceptions
#FINALLY: do this no matter what happens
#RAiSE: RAISING YOUR OWN EXCEPTIONS

#FileNotFoundError
# try:
#     file = open("text.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("text.txt", "w")
#     file.write("Something")
#     file.close()
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up")






# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary[["non_existing_key"]]

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# #TypeError
# text = "abc"
# print(text + 5)


height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2

