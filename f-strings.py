letter = 'My name is {1} , I am from {0}'
name = 'Chandan'
city = 'Bangalore'

print(letter.format( city,name))
print(f'We use f-strings like this: my name is {{1}}, I am from {{0}}')  # Displaying raw f-strings
# print(f'My name is {name} , I am from {city}')

price = 49.0099
txt= f'For only {price:.2f} dollors'
print(txt)