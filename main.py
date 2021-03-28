import quiz_brain
from data import question_data
from question_model import Question

question_bank = []

for ques in question_data:
    question = Question(text=ques['question'], ans=ques['correct_answer'])
    question_bank.append(question)

quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print('You have completed the quiz!')
print(f'Your final Score is: {quiz.score}/{quiz.question_no}')
