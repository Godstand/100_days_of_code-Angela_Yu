sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
# converting a sentence into a list
sentence_list = sentence.split()
# creating a dictionary using dictionary comprehension where the length of each word is assigned as a key value
result = {word: len(word) for word in sentence_list}

print(result)
