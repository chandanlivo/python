# wayne = {2, 3}
# print(type(wayne)) >>>>>>>>output is dictionary 

# METHODS

# UNION
# s1 = {1,2,4,5}
# s2 = {3,5,6}
# print(s1.union(s2))
# s1.update(s2)
# print(s1,s2)

# INTERSECTION
# cities = {'madrid', 'turin', 'manchester', 'munich'}
# cities2 = {'tokyo', 'madrid', 'munich','bayer'}
# print(cities.intersection(cities2)) # below line also prints same output
# cities.intersection_update(cities2)
# print(cities)

# SYMMTERIC DIFFERNCE
# cities = {'madrid', 'turin', 'manchester', 'munich'}
# cities2 = {'tokyo', 'madrid', 'munich','bayer'}
# print(cities.symmetric_difference(cities2)) # below line also prints same output
# cities.symmetric_difference_update(cities2)
# print(cities)

cities = {'madrid', 'turin', 'manchester', 'munich'}
cities2 = {'delhi', 'madras'}
cities3 = {'delhi', 'madras','madrid'}
# print(cities2.isdisjoint(cities))
# print(cities2.issubset(cities3))
# cities.discard('tokyo')
# print(cities)
# item = cities.pop()
# print(item)
# del cities
# cities.clear()
print(cities)
if 'madrid' in cities:
    print('madrid is present')
else:
    print('madrid is not present')
