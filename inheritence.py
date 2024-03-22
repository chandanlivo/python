class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showdetails(self):
        print(f'The name of employee {self.id} is {self.name}')

class Programmer(Employee):
    def showlanguage(self):
        print('The default language is python')

e1=Employee('chandan', 11)
e1.showdetails()
e2 = Programmer('hemanth', 10) # Can access the class Employee
e2.showdetails()
e2.showlanguage()