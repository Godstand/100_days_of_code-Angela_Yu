student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# looping through a dictionary
# for (key, value) in student_dict.items():
#     print(value)

import pandas
# student_dict_dataframe = pandas.DataFrame(student_dict)
# print(student_dict_dataframe)
# loop through a dataframe
# for (key, value) in student_dict_dataframe.items():
#     print(value)
# loop through each row in the dataframe
# for (index, row) in student_dict_dataframe.iterrows():
#     if row.score > 60:
#         print(row.student)
# using dictionary comprehension
# print([row.student for (index, row) in student_dict_dataframe.iterrows() if row.score > 60])

# TODO 1. Create a dictionary in the format of a list
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of phonetic code words from a word that the user inputs
user_input = input("Enter the word: ").upper()
phonetic_code = [phonetic_dict[letter] for letter in user_input]
print(phonetic_code)

