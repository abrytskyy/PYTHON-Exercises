from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question1 = Question(question["text"], question["answer"])
    question_bank.append(question1)

quiz = QuizBrain(question_bank)
while
quiz.next_question()