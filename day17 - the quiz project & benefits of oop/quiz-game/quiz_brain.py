class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        self.user_answer = input(f'Q.{self.question_number + 1} {self.question_list[self.question_number].question} (True/False)?: ')
        self.check_answer()

    def still_has_questions(self):
        self.question_number += 1
        if self.question_number < len(self.question_list):
            return True
        else:
            print("You've completed the quiz!")
            print(f'Your final score is {self.score}/{self.question_number}')
    
    def check_answer(self):
        if self.user_answer.lower() != self.question_list[self.question_number].answer.lower():
            print('Wrong.')
        else:
            print('Correct!')
            self.score += 1
        print(f'The correct answer is: {self.question_list[self.question_number].answer}')
        print(f'Your score is {self.score}/{self.question_number + 1}')
        print()