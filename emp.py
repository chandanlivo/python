class Employee:
    # def __init__(self, name):
    #     self.name = name 
    name = 'Chandan'
    def __len__(self):
        i = 0 
        for c in self.name:
            i = i+ 1
        return i
    