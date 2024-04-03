class Mother:
    mothername = "Seetha"

    def mother(self):
        print(self.mothername)

class Father:
    fathername = "Ram"

    def father(self):
        print(self.fathername)

class Son(Father, Mother):
    def parent(self):
        print('Father name = ', self.fathername)
        print('Mother name = ', self.mothername)

s1 = Son()
# s1.fathername = 'Ram'
# s1.mothername = 'Seetha'
s1.parent()