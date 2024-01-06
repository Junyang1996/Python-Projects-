from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

# TODO 1
# question bank, we will use it later as reference
for item in question_data:
    to_add = Question(item["text"], item["answer"])
    question_bank.append(to_add)

Quiz1 = QuizBrain(question_bank)
Quiz1.next_question()
