class Employee:
    def __init__(self):
        self.__name = 'chandan'
a  = Employee()
# print(a.__name)  Cannot be accessed directly
print(a._Employee__name) # can be accessed indirectly
print(a.__dir__())