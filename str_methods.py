str1 = "he's a boy and is name as chandan"
print(str1.find('is')) # returns -1
#print(str1.index('is'))  # raises an exception if fails to fetch the provided string
str2 = "CristianoRonaldo7" # RETURNS FALSE EVEN SPACE IS PRESENT WITHIN THE STRING
print(str2.isalnum())
print(str2.isalpha())
print(str2.replace("CristianoRonaldo7", "Siuuu7"))