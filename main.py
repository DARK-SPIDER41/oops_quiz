from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
question_text = ''
question_answer = ''
for i in question_data:
    # question_text = i['text']
    # question_answer = i['answer']
    # new = Question(question_text, question_answer)
    new = Question(i['question'], i['correct_answer'])
    question_bank.append(new)
# print(question_bank[0].text)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("you have completed the quiz")
print(f"your final score was : {quiz.score}/{quiz.question_number}")
