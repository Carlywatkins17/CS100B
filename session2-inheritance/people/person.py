class Person:

    def __init__(self, name='', ID=-1, birthdate='1/1/2000'):
        self.name = name
        self.ID = ID
        self.birthdate = birthdate

    def eat(self):
        print(self.name + ' is taking a diner break.')

    def sleep(self):
        print(self.name + ' is sleeping.')

    def intro(self):
        print('Hello.  My name is ' + self.name)