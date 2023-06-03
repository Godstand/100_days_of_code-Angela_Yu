from question_model import Question
class QuizBrain:

    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_guess = input(f"Q.{self.question_number}: {current_question.text} (True or False):").lower()
        correct_answer = current_question.answer.lower()
        self.check_answer(user_guess, correct_answer)

    def check_answer(self, user_guess, correct_answer):
        if user_guess == correct_answer:
            self.score += 1
            print("You got it right")
        else:
            print("Oh, that's not correct. Try again later!")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{len(self.question_number)}")

