# import requests
#
# parameters = {
#     "amount": 10,
#     "type": "boolean"
# }
#
# response = requests.get("https://opentdb.com/api.php", params=parameters)
# response.raise_for_status()
# data = response.json()
# question_data = data["results"]


question_data = [
     {"category": "Animals",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The Axolotl is an amphibian that can spend its whole life in a larval state.",
      "correct_answer": "True", "incorrect_answers": ["False"]},
     {"category": "Animals", "type": "boolean", "difficulty": "easy",
      "question": "Kangaroos keep food in their pouches next to their children.",
      "correct_answer": "False", "incorrect_answers": ["True"]},
     {"category": "Animals", "type": "boolean", "difficulty": "easy",
      "question": "A bear does NOT defecate during hibernation. ",
      "correct_answer": "True", "incorrect_answers": ["False"]},
     {"category": "Animals", "type": "boolean", "difficulty": "easy",
      "question": "In 2016, the IUCN reclassified the status of Giant Pandas from endangered to vulnerable.",
      "correct_answer": "True", "incorrect_answers": ["False"]},
     {"category": "Animals", "type": "boolean", "difficulty": "easy",
      "question": "A flock of crows is known as a homicide.",
      "correct_answer": "False", "incorrect_answers": ["True"]},
     {"category": "Animals", "type": "boolean", "difficulty": "easy",
      "question": "A caterpillar has more muscles than humans do.",
      "correct_answer": "True", "incorrect_answers": ["False"]},
     {"category": "Animals", "type": "boolean", "difficulty": "easy",
      "question": "Cats have whiskers under their legs.",
      "correct_answer": "True", "incorrect_answers": ["False"]},
     {"category": "Animals", "type": "boolean", "difficulty": "easy",
      "question": "Rabbits are carnivores.", "correct_answer": "False",
      "incorrect_answers": ["True"]},
     {"category": "Animals", "type": "boolean", "difficulty": "easy",
      "question": "The internet browser Firefox is named after the Red Panda.",
      "correct_answer": "True", "incorrect_answers": ["False"]},
     {"category": "Animals", "type": "boolean", "difficulty": "easy",
      "question": "The freshwater amphibian, the Axolotl, can regrow it&#039;s limbs.",
      "correct_answer": "True", "incorrect_answers": ["False"]}
]
