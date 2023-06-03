# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
#
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"
# Open invited name and read content. Convert all lines to a list
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
# Open the starting letter file and read content.
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        # remove all spaces from the list
        stripped_name = name.strip()
        # replace all placeholders with the stripped names
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # create new txt documents for each letter
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letters:
            completed_letters.write(new_letter)

