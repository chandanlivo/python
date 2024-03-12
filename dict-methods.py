ep1 = {101:56, 123:76, 143:66, 154:80}
ep2={222:57, 554:87}

# ep1.update(ep2)
# print(ep1)

# ep1.clear()
# print(ep1)

# ep1.pop(123)
# print(ep1)

ep1.popitem()
print(ep1)

del ep1[101]
print(ep1)