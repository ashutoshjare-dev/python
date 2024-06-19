# Data types
# integer, string, list, tuple, dictionary, set 

## Numbers
# num:int = 2 # :int is a type hint. They are used to indicate the type of a variable, parameter, or return value, but they do not enforce type checking at runtime.
num = 2 # integer

# Arithmetic operations
2+2 # Addition
2-2 # Subtraction
2*2 # Multiplication
2/2 # Division
2//2 # Floor division
3%2 # Reminder is returned after division
3**2 # Square of a number
4**(1/2) # Square root of a number

# NOTE: In interactive mode, the last printed expression is assigned to the variable _.

## String/Text
name = "Ashutosh" # string
"Some text"
'Some text'
'doesn\'t'  # use \' to escape the single quote...
# output -> "doesn't"

"doesn't"  # ...or use double quotes instead
# output -> "doesn't"
'"Yes," they said.'
# output -> "Yes," they said.
"\"Yes,\" they said."
# output -> "Yes," they said.
'"Isn\'t," they said.'
# output -> "Isn\'t," they said.

s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), special characters are included in the string
# output -> 'First line.\nSecond line.'
print(s)  # with print(), special characters are interpreted, so \n produces new line
# output -> First line.
# output -> Second line.
# output -> 

# slicing string
word = 'Python'
word[0]  # character in position 0
# output -> 'P'
word[5]  # character in position 5
# output -> 'n'
word[-1]  # last character
# output -> 'n'
word[-2]  # second-last character
# output -> 'o'
word[0:2]  # characters from position 0 (included) to 2 (excluded)
# output -> 'Py'
word[2:5]  # characters from position 2 (included) to 5 (excluded)
# output -> 'tho'
word[:2]   # character from the beginning to position 2 (excluded)
# output -> 'Py'
word[4:]   # characters from position 4 (included) to the end
# output -> 'on'
word[-2:]  # characters from the second-last (included) to the end
# output -> 'on'
"The sum of 1 + 2 is {0}".format(1+2)
# output -> 'The sum of 1 + 2 is 3'
print('%(language)s has %(number)03d quote types.' %
      {'language': "Python", "number": 2})
# output -> Python has 002 quote types.



## List
list1 = [1,2,3,"abc", ["lmn", "xyz", 456]] # list. It can have multiple data types stored in it.

squares = [1, 4, 9, 16, 25]
squares
[1, 4, 9, 16, 25]
squares[0]  # indexing returns the item
1
squares[-1]
25
squares[-3:]  # slicing returns a new list
[9, 16, 25]

# Lists also support operations like concatenation:
squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# # for python 3.10 or newer
# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"

