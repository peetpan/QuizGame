class QuizBrain:
    def __init__(self, question_bank):
        self.question_no = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        ques = self.question_list[self.question_no].text
        correct_ans = self.question_list[self.question_no].answer
        self.question_no += 1
        user_ans = input(f"Q{self.question_no}. {ques} (True/False): ")
        self.check_correct_ans(user_ans, correct_ans)

    def check_correct_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print('You\'re right')
        else:
            print('That\'s wrong')
        print(f'The correct answer is {correct_ans}')
        print(f'Your current score = {self.score}/{self.question_no}')
        print('\n')

    def still_has_question(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            return False
