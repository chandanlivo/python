#def average(a= 9, b= 1):
#    print('The average is:', (a+b)/2)
#average(4, 6)
#average(a=4)

#def name(fname, mname = 'Shree ', lname ='Ram'):
#    print('Hello',fname, mname, lname)
#name('Jai', 'Shree', 'Krishna')
    
def average(*numbers):
    print(type(numbers))
    print('length of numbers is:', len(numbers))
    
    sum = 0
    for i in numbers:
        sum = sum + i
    #print('avg is:', sum/len(numbers))
    return sum/len(numbers)

c = average(5,6,7,6)
print(c) #--- STORES VALUE IN "C"---