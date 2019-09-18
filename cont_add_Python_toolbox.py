REPL, a read-eval-print-loop

-i flag to python (or ipython). python -i myscript.py



################# string #################
'abc' != 'def'
True
'abc' + 'def'

'abcdef'
'abc' * 3

'abcabcabc'

% formatting: a little older, but still fairly common
.format: a newer way to format strings
f-strings: introduced in python 3.6; comparable to string interpolation in other languages


name = 'world'
print('hello, %s!' %name)
print('hello, {}!'.format(name))
print(f'Hello, {name}!')


.lower and .upper: convert the string to all lower or upper case
.strip: remove any leading and trailing whitespace from the string
.isdigit: test whether or not the string is a number
.split: convert a string to a list
.join: convert a list to a string



All of the string methods here do not modify the original string, 
they return a new string with the modification.
Unless it was store/assigned into a variable then you can retrieve



################# list #################
[n * 2 for n in range(10) if n % 2 == 0]

numbers = [1, 2, 3]
numbers.append(4)	>>	[1, 2, 3, 4]
numbers.pop()	>>	[1, 2, 3] # pop out the last one
numbers.remove(4) >> [1,2,3] # remove the specific value
len(numbers)

numbers[0] # the first element in the list

## Slice
numbers[:2] # everything up to, but not including, the element at index 2
[1, 2]

numbers[1:2] # everything from index 1 up to, but not including, index 2
[2]

numbers[1:] # everything from index 1 to the end of the list
[2, 3]

return an iterable
range >> iterable range object, not a list
list(range(10)) >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list('abcdef') >> ['a', 'b', 'c', 'd', 'e']
list(map(str, [1, 2, 3]))
  
# Return double of n 
def addition(n): 
    return n + n 
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 

# Double all numbers using map and lambda 
numbers = [1,2,3,4]
result = map((lambda n: n + n for n in numbers), numbers) 
print(list(result))
""" 
TypeError                                 Traceback (most recent call last)
<ipython-input-28-c0896bf7a938> in <module>
      1 numbers = [1,2,3,4]
      2 result = map((lambda n: n + n for n in numbers), numbers)
----> 3 print(list(result))

TypeError: 'generator' object is not callable
"""
 
numbers = [1,2,3,4]
result = map(lambda x: x + x, numbers) 
print(result)
"""
In [30]: numbers = [1,2,3,4] 
    ...: result = map(lambda x: x + x, numbers)  
    ...: print(result)                                                                                                                      
<map object at 0x102dc7ef0>

"""

numbers = [1,2,3,4]
result = map(lambda x: x + x, numbers) 
print(list(result)) # [2, 4, 6, 8]

## list comprehension
transform one iteable item(ex: list) into another(ex:list)
elements can be conditionally included or transformed in new list

new_things = []
for item in old_things:
	if condtion_based_on(item):
		newthings.append("something with " + item)
new_things = ["something with" + item for item in old_things if item in condition_based_on(item)]

numbers = [1,2,3,4]
doubled_odds = [n*2 for n in numbers if n%2 == 1]
doubled_odds


numbers = [1,2,3,4]
doubled_odds = []
for n in numbers:
	if n % 2 != 0:
		doubled_odds.append(n * 2) 
doubled_odds

numbers = [1,2,3,4]
double_num = []
for n in numbers:
	double_num.append(n*2)
doubled_num

numbers = [1,2,3,4]
doubled_num = [n*2 for n in numbers]
doubled_num

##################### Tuple #######################

DON'T QUITE GET immutable, once established, can't cahnge them?
x = ('abc')                                                                                                                        

In [35]: x.upper()                                                                                                                          
Out[35]: 'ABC'

In [36]: x                                                                                                                                  
Out[36]: 'abc'

index = check
commonly used to store different data types
list are used for all same data type
EX: tuple_example = (1, 'one',[1])

##################### Dictionary #######################
{"key":"value"} 
created by writing a dictionary literal, which is delimeted with curly braces
keys are separated from the values with a colon, and key-value pairs are separated by commas.

created with the built-in dict function:
x = {}
x = dict(name='Codeup', age=4)
x
{'name': 'Codeup', 'age': 4}

# access dic just like list
school['name']
'Codeup'

In [46]: school = {"name":"Codeup","age":4}                                                                                                 
In [47]: school["age"] += 1                                                                                                                 
In [48]: school                                                                                                                             
Out[48]: {'name': 'Codeup', 'age': 5}

me = {'name': 'JQ'}
me['name'] = 'JQ'
me['name'] = me['name'].lower() >>  {'name': 'jq'}
me['capitalized_name'] = me['name'].capitalize() >> {'name': 'jq', 'capitalized_name': 'Jq'}

Code that makes a new dictionary by swapping the keys and values of the original one:
new_dic = {v: k for k, v in school.item()}

new_dic = {}
for k, v in school.items():
	new_dic[v] = k
new_dic

Code that creates a set of all the first letters in a sequence of words:

first_letters = set()
for w in words:
    first_letters.add(w[0])

first_letters = {w[0] for w in words}

flattened = []
for row in matrix:
    for n in row:
        flattened.append(n)
flattened = [n for row in matrix for n in row]

doubled_numbers = []
for n in numbers:
    doubled_numbers.append(n * 2)
doubled_numbers = [n * 2 for n in numbers]




##################### control structure #######################

conditionals: allow us to execute code conditionally
loops: allow us to execute code repeatedly

if
keyword if
a condition that evaluates to a boolean value followed by a colon (:)
the body of the statement indented by 4 spaces




while loop will execute it's body until the condition evaluates to false

i = 5
while i <= 10: # false when i > 10, break
    print(i)
    i += 1

 If the condition in the while loop never evaluates to False, you will end up with 
 what is called an infinite loop


 2 special keywords in Python that can change how the control flows through a loop:

continue will skip to the next iteration of a loop
break will stop executing the loop entirely



def factorial(number):
	if number == 1:
		return number
	else:
		return number*factorial(number-1)




dataset = [{'name': 'age', 'type': 'int', 'data': [20, 25, 43, 11, 15, 53, 36]},
           {'name': 'is_vegetarian', 'type': 'boolean', 'data': [False, True, False, False, True, False, False]},
           {'name': 'shoe size', 'type': 'int', 'data': [8, 11, 7, 10, 7, 9, 10]},
           {'name': 'ISP', 'type': 'categorical', 'data': ['AT&T', 'Spectrum', 'Spectrum', 'Spectrum', 'AT&T', 'Spectrum', 'AT&T']},
           {'name': 'BMI', 'type': 'float', 'data': [29.9, 20.4, 23.3, 21.7, 22.2, 22.8, 27.0]}]

# print the means for the numeric data
for feature in dataset:
    if feature['type'] == 'categorical' or feature['type'] == 'boolean':
        print('{} is not numeric, skipping'.format(feature['name']))
        continue # with the control flow, continue, skip the items that can't be calculated
    avg = sum(feature['data']) / len(feature['data'])
    print('{} average: {:.2f}'.format(feature['name'], avg))

>>>
age average: 29.00
is_vegetarian is not numeric, skipping
shoe size average: 8.86
ISP is not numeric, skipping
BMI average: 23.90


 ########################
 import std lib (json, collection, itertools, math)
 anaconda (include some popular 3rd party pkgs)
 install 3rd party (matplotlib, beautifulsoup, numpy, pandas)


 'bayes' # string literal
 1+1 #1 iter
 operator + can mean plus or concat
 '1'+'1' > '11'
 'a' * 3 > 'aaa' 
 ### don't assume numbers are numbers, always check type or assing int or float if absolutely need a number
 max(['1','2','3','10']) > 3 #when it's string, it will be sorted alphabetically instead of number


# double all with lambda and map
# map(______,_________) rule map to target
# if not holding the result in list, the result will be a generator object, not callable
numbers = [1,2,3,4]
result = list(map(lambda x: x + x , numbers))
result

# nested loop with list comp
flattened = [n for row in matrix for n in row]

flattened = []
for row in matrix:
	for n in row:
		flattened.append(n)
# get the first alphabet, but unique/non-repeatative (using set) for each word in a list of words
words = ['apple','banana','bank']
first_letter = set()
for word in words:
	first_letter.add(word[0])
first_letter

# get the list of first alphabet for each word in  a list of words
first_lette = [w[0] for w in words]
first_lette

# turn list into set
set(first_lette)




 pwd #right dir
 python -m doctest file_name.py # nothing if all correct!
