#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./input/Names/invited_names.txt") as file:
    names = file.readlines()
    new_names_list = []

with open("./input/Letters/starting_letter.txt") as letter_file:
    for name in names:
        strip_name = name.strip()
        starting_letter = letter_file.read()
        finished_letter = starting_letter.replace("[name]", strip_name)
        print(finished_letter)

        with open(f"./Output/ReadyToSend/letter_for_{strip_name}.txt", "w") as ready_to_send:
            ready_to_send.write(finished_letter)

