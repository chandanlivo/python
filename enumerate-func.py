marks = [22,32,45,55,67,876,4,73,61]

# index = 0 
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print('HI I AM AN INDIAN')
#     index += 1

for index, mark in enumerate(marks,start = 2):
    print(mark)
    if index == 4:
        print('Hey, its awesome')