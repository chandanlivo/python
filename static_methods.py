def add(a, b):
        return a + b 

class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):  # while using static methods , we are not forced to use "SELF"
        return a + b
    
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
# x = a.add(2, 7)
# print(x)
print(a.add(2, 7))  # called using name of an instance 
print(Math.add(2, 7)) # can be called using name of the class or an instance
print(add(2,7))  # defined outside the class