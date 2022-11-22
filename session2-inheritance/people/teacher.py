from person import Person

class Teacher(Person):

    def __init__(self, name='', ID=-1, birthdate='1/1/2000'):
        Person.__init__(self, name, ID, birthdate)

    def teach(self):
        print(self.name + ' is teaching.')

    def define_homework(self, course):
        print(self.name + ' assigned homework for their ' + course + ' course.')

    def answer_question(self):
        print('It is due next Monday.')

    def intro(self):
        print('Welcome, class.  I am professor ' + self.name)

