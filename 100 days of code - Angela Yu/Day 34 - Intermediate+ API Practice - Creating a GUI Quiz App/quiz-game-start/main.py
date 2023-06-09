from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from html import unescape
from ui import QuizInterface

# create an emply question bank
question_bank = []

# create a for loop to iterate over the question_bank
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(unescape(question_text), question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

quiz_Interface = QuizInterface(quiz)


# while quiz.still_has_questions():
#     # if quiz still has remaining question
#     print(f"Your current score is {quiz.score}/{len(quiz.question_list)}")
#     quiz.next_question()

print("You have completed the quiz")
print(f"Your final is {quiz.score}/{len(quiz.question_list)}")
