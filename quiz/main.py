from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question = i['text']
    answer = i['answer']
    q_a = Question(question, answer)
    question_bank.append(q_a)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

