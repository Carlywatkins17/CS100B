class questions:

    def __init__(self, question_text='', correct_answer='', number='', weight=''):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.number = number
        self.weight = weight


    
    def display_question(self, question_text):
        print(question_text)


