class QuizBrain:
    def __init__(self, p_question_list):
        self.question_number = 0
        self.question_list = p_question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        correct_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question} (True/False)?: ")
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, p_user_answer, p_correct_answer):
        if p_user_answer.lower() == p_correct_answer.lower():
            self.score += 1
            print("You got it right.")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {p_correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
