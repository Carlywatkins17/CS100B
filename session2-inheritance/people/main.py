from person import Person
from teacher import Teacher
from student import student 
from staff import staff

def main():
    people = [Teacher('Pete'), student('Carly'), staff('Jackie', '3', '06/23/1970', 'receptionist')]

    for p in people: 
        p.intro()
        p.sleep()
        p.eat()

        if type(p) is Teacher:
            p.teach()
        elif type(p) is student:
            p.ask_question()
        elif type(p) is staff:
            p.name_role()
       

if __name__ == '__main__':
    main()