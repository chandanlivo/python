f = open('myfile.txt', 'r')
print(type(f))

f.seek(3) #move to the 10th of the file
print(f.tell())
data = f.read(6) # read the next 5 bytes

print(data)