class Employee:
    company = 'Apple'
    def show(self):
        print(f'My name is {self.name} working in {self.company}')

    @classmethod
    def changeCompany(self, newCompany):
       self.company = newCompany

e1 = Employee()
e1.name = 'Harry'
e1.show()
e1.changeCompany('Google') 
e1.show()
print(Employee.company)