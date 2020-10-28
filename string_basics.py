# Type	     Examples                               Naming Convention
# Function --> function, my_function      -->	Use a lowercase word or words. Separate words by underscores to improve readability.
# Variable --> x, var, my_variable	    --> Use a lowercase single letter, word, or words. Separate words with underscores to improve readability.
# Class	 --> Model, MyClass             --> Start each word with a capital letter. Do not separate words with underscores. This style is called camel case.
# Method   --> class_method, method       --> Use a lowercase word or words. Separate words with underscores to improve readability.
# Constant --> CONSTANT, MY_CONSTANT,     --> Use an uppercase single letter, word, or words. Separate words with underscores to improve readability.	CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT
# Module	 --> module.py, my_module.py    --> Use a short, lowercase word or words. Separate words with underscores to improve readability.
# Package	 --> package, mypackage         --> Use a short, lowercase word or words. Do not separate words with underscores.

#####    https://www.learnbyexample.org/python-string-replace-method/
#
# https://www.learnbyexample.org/python-set/

import re
soup="Spicedcarrot&lentilsoup"
salad='Ceasarsalad'
###  STRING LENGTH
print(len(soup))
print(len(salad))

###  STRING FORMAT
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "For only {price:.5f} dollars!"
print(txt1.format(price=49))

S = '42'
x = '{:0>6}'.format(S)
print(x)

txt1 = "My name is {fname}, I'am {age}".format(fname="John", age = 36)
txt2 = "My name is {0}, I'am {1}".format("John",36)
txt3 = "My name is {}, I'am {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)

###  STRING REPLACE
print("STRING REPLACE:", soup )
soup = soup.replace("&","")
print(soup)

###   RINDEX  &  RFIND
print("Printing Right Index of 'rot' from String soup:", soup.rindex("rot"))
test_string = "CarrotParrotErroticRotten"
print("Printing right most index of case sensitive word 'rot':", test_string.rfind("rot"))
print(test_string.rindex('rot'))   ## rindex means, we are explictly saying 'rot' word contains, if it is not there, it'll throw Triggers ValueError: substring not found

####  print(test_string.rindex('zebra')) ## ValueError: substring not found
print(test_string.rfind('zebra'))  ## If Not found, throws "-1"  --> safe exit from code

###  FORMAT_MAP
# input stored in variable a.
a = {'x': 'John', 'y': 'Wick'}
# Use of format_map() function   ## We Should know Keys before hand
print ("{x}'s last name is {y}".format_map(a))

#### STRING STARTSWITH
print("{x}'s last name is {y}".format_map(a).startswith("S"))
print("{x}'s last name is {y}".format_map(a).startswith("J"))
print("{x}'s last name is {y}".format_map(a).find("Wick"))  ### Gives index of 'Wick'

print(test_string.count('rot'))
print(test_string.count('Rot'))

pattern = re.compile(r'(?i)(rot)')
print(pattern.findall(test_string))

###  STRING CONCAT & JOIN DIFFERENCE
# concatenation operator
x = 'aaa' + 'bbb'
print(x)
# Prints aaabbb

# join() method
x = '-'.join(['aaa','bbb'])
print(x)
# Prints aaabbb