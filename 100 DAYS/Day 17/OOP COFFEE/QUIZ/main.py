from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# question1 = Question("A slug's blood is green.", "True")
# print(question1.__dict__)

question_bank = []
for question in question_data:
    if question["text"] not in question_bank:
        question_new = Question(question["text"], question["answer"])
        question_bank.append(question_new)

quiz = QuizBrain(question_bank)
quiz.next_question()