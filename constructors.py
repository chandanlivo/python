class person:

    def __init__(self, name, occ):  #  this method is called whenever a new object is created out of the class
                               # self is automatic , n and o will map to name and occ respcvly
        print('Hey how are you')
        self.name = name
        self.occ = occ

    def info(self):
        print(f'{self.name} is a {self.occ}')

a = person('chandan', 'engg') 
b = person('amat', 'driver')
a.info() 
b.info()