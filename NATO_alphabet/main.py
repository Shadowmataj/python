import pandas


# numbers = [1, 2, 3]
#LIST COMPREHENSION
#new_list = [new_item for item in list]
# new_list = [number + 1 for number in numbers]

# name = "Christian"
# new_list = [letter for letter in name]

#CONDITIONAL LIST COMPREHENSION
#new_list = [new_item for item in list if test]
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_list = [name.upper() for name in names if len(name) > 5]
# print(new_list)

#DICTIONARY COMPREHENSION
#new_dict = { new_key: new_value for item in list }
#new_dict = { new_key: new_value for (key, name) in dict.items() }

#CONDITIONAL DICTIONARY COMPREHENSION
#new_dict = { new_key: new_value for (key,value) in dict.items() if test }


# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# students_score = {
#     name: random.randint(1,100) for name in names
# }
#
# passed_students = {
#     name: "Passed" for (name, score) in students_score.items() if score > 60
# }
#
#
# print(students_score)
# print(passed_students)


# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(data_dict)

error = True
while error:
        word = input("Write your word: ").upper()
    try:
        nato_list = [data_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        error = not error

print(nato_list)
