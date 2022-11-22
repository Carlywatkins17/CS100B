from person import Person

class student(Person):

    def __init__(self, name='', ID=-1, birthdate='1/1/2000'):
        Person.__init__(self, name, ID, birthdate)

    def study(self):
        print(self.name + ' is studying')

    def do_homework(self, course):
        print(self.name + ' is doing homework for their ' + course + ' course.')

    def ask_question(self):
        print('When is this due?')

    def intro(self):
        print('Sup. Names lil ' + self.name)
 