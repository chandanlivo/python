#READING A FILE

# f= open('myfile.txt', 'r') # If no argument is passed , read is the default
# text = f.read()
# print(text)
# f.close()

#WRITING INTO A FILE

# f= open('myfile.txt', 'a')
# f.write('---Hello, World----')
# f.close()

with open('myfile.txt', 'a') as f:
    f.write('Hello World\n')