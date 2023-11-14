class QuizBrain:
    def __init__(self, q_list):
        self.questions_list = q_list
        self.questions_number = 0
    def next_question(self):
        current_question = self.questions_list[self.questions_number]
        self.questions_number += 1
        input(f"Q.{self.questions_number}: {current_question.text} (True/False):")


