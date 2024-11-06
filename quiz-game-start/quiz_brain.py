class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)



    def next_question(self):
        new_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}: {new_question.text} (True/False): ")
        self.check_answer(user_answer, new_question.answer)

    def check_answer(self, u_answer, q_answer):
        if u_answer.lower() == q_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {q_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")