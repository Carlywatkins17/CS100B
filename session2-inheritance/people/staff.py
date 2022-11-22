from person import Person

class staff(Person):
    
    def __init__(self, name='', ID=-1, birthdate='1/1/2000', role=''):
        Person.__init__(self, name, ID, birthdate)
        self.role = role

    def name_role(self):
        print(self.name + ' is a ' + self.role)

    def sched(self):
        print(self.name + ' works ' + 'Mon-Fri.')