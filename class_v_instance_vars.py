class employee:
    comp_name= 'TATA' # class variable
    no_of_empos = 0
    def __init__(self, name, raise_amt):
        self.name = name
        # self.raise_amt = 0.02
        self.raise_amt = raise_amt
        employee.no_of_empos += 1
    def showdetails(self):
        print(f'The name of employee is {self.name} sized {self.no_of_empos} and the raise amount in {self.comp_name} is {self.raise_amt}')

e1= employee('Chandan',0.02)
e1.comp_name = 'TATA ELIXSI' #instance variable 
e1.showdetails()
# employee.showdetails(e1)## same as the above line
employee.comp_name= 'google' # takes before the class variable
e3 = employee('Rio', 2.2)
employee.showdetails(e3)