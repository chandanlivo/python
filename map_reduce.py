#MAP
#  def cube(x):   WE CAN USE LAMBDA INSTEAD OF THIS 
#      return x*x*x

l= [1,2,3,4,5]

#  newl = []
#  for item in l:
#      newl.append(cube(item))
#  print(newl)

#  newl = list(map(lambda x:x*x*x , l))
#  print(newl)

# #FILTER
def filter_function(l):
 return l > 3

newnewl = list(filter(filter_function, l))
print(newnewl)


#REDUCE
from functools import reduce
numbers = [1,2,3,4,5]
sum= reduce(lambda x,y : x+y , numbers)
print(sum)
