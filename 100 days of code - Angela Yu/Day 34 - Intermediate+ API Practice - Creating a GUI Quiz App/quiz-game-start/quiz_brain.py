class QuizBrain:

    def __init__(self, q_list):
        self.q_text = None
        self.question_list = q_list
        self.question_number = 0
        self.score = 0
        self.current_question = None

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.q_text = self.current_question.text
        return f"Q.{self.question_number}: {self.q_text}"
        # user_guess = input(f"Q.{self.question_number}: {current_question.text} (True or False):").lower()
        # correct_answer = current_question.answer.lower()
        # self.check_answer(user_guess, correct_answer)

    def check_answer(self, user_guess):
        correct_answer = self.current_question.answer
        if user_guess.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
