names = "Chandu, Hemu"
print(names[0:6])
print(len(names))
fruit = "mango"
len1 = len(fruit)
print('mango is a' ,len1, 'letter word')
print(fruit[0:3]) #including 0 ,but not 3
print(fruit[1:3]) # including 1 but not 3 
print(fruit[-3:-1]) #  including [5-3=2] but not [5-1=4]
print(fruit[0:-3])  #removes last 3 char's of the string
# the above and the below lines are the same
print(fruit[0:len(fruit)-3])
print(fruit[-1:len(fruit)-3]) #wont print anything
print(fruit[:3])
print(fruit[:]) #prints mango