f = open('myfile.txt', 'w')
f.write('hello world')
f.truncate(5)

f = open('myfile.txt', 'r')
print(f.read())