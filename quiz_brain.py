class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(answer, question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, cur_answer):
        if answer.lower() == cur_answer.lower():
            self.score += 1
            print("you got it right")
        else:
            print("that's wrong")
        print(f"the correcct answer was : {cur_answer}")
        print(f"your current score is {self.score}/{self.question_number}\n")
