from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

# TODO 1
# question bank, we will use it later as reference
for item in question_data["results"]:
    to_add = Question(text=item["question"], answer=item["correct_answer"])
    question_bank.append(to_add)

Quiz1 = QuizBrain(question_bank)

while Quiz1.still_have_questions():
    Quiz1.next_question()

print("\n\n")
print("You've completed this quiz")
print(f"Your final score was: {Quiz1.score}/{Quiz1.question_number}")
