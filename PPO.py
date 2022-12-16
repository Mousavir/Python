from dataclasses import dataclass

class Person:
    def __init__(self):
        self.name = ''

class Student(Person):
    def __init__(self):
        super().__init__()

        self.id =  0

audrey = Person()
audrey.name = 'Audrey'

eleve_1 = Student()
eleve_1.name = 'Jean'
eleve_1.id = 123456