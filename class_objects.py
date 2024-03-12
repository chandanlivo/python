class person:
    name = "chandan"
    occupation ="Engineer"
    networth = 10
    def info(self):
        print(f'{self.name} is a {self.occupation}') # reference to the current instance of class and is used to access the variables 
                                                       #that belongs to the class

a = person()
b =person()
c= person()
a.name = "babu"
a.occupation = "Nurse"

b.name = "harry"
b.occupation = "developer"
# print(a.name, a.occupation) 
a.info()
b.info()
c.info() # returns the default value i.e chandan