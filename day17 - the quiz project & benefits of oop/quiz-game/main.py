from question_model import Question
from data import question_data, question_data_2
from quiz_brain import QuizBrain

question_bank = []

# ###setup for question_data
# for item in question_data:
#     question_bank.append(Question(item['text'], item['answer']))

###question fro question_data_2
for item in question_data_2['results']:
    question_bank.append(Question(item['question'], item['correct_answer']))


if len(question_bank) != 0:
    quiz = QuizBrain(question_bank)

    quiz.next_question()

    while quiz.still_has_questions():
        quiz.next_question()