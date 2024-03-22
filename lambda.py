def app(ff, value):
    return 6 + ff(value)
double = lambda x : x*2

avg = lambda c,d : (c+d)/2
# cube = lambda x : x*x*x  This can be used in app without defining it as cube
print(double(5))
# print(cube(4))
print(avg(5,9))
print(app(lambda x : x*x*x, 2)) # without defining cube we can use lambda directly while printing the app fuction   