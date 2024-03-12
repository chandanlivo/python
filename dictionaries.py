# info = {'name':'chandan', 'age':'21', 'eligible':'yes'}
# # print(info)
# print(info['age']) #throws error
# print(info.get('age')) # does not throw error

# info = {'name':'chandan', 'age':'21', 'eligible':'yes'}
# print(info.keys())
# print(info.values())

# for key in info.keys():
#     # print(info[key])
#     print(f'The value corresponding to the key {key} is {info[key]}')

info = {'name':'chandan', 'age':'21', 'eligible':'yes'}
print(info.items())

for key, value in info.items():  #prints same as the above for loop
    print(f"The value corresponding to the key {key} is {value}")

    