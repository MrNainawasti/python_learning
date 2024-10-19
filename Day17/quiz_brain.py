class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self, question_bank):
        return self.question_number < len(question_bank)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number}: {current_question.text}(True/False): ").lower()
        return user_answer

    def score_check(self, user_choice):
        current_question = self.question_list[self.question_number - 1]
        right_answer = current_question.answer
        if user_choice == right_answer.lower():
            print("You got it right!")
            print(f"The correct answer was: {right_answer}")
            self.score += 1
        else:
            print("Wrong answer!")
            print(f"The correct answer was: {right_answer}")

        print(f"your current score is: {self.score}/{self.question_number}\n")
         
    def end_quiz(self):
        print("Congratulations!!You've completed the quiz.")
        print(f"your final score is: {self.score}/{self.question_number}.")










    
