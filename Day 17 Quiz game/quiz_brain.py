class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.list = question_list

    def next_question(self):
        """retrieve the current question from the current question number and ask the question to the user"""
        answer = input(f"Q. {self.question_number+1}: {self.list[self.question_number].text} (True/False)?: ")

