print("string1","string2")

print("string1", "string2", sep="======") # sep can be customized what separates the elements (by default the "," just prints a space)

# \n : new line charector, \t : tab character
print("string1\n\n\n")
print("^^^ This just shows the space made with the 3 \n new line characters")

# \t : tab character
print("This is a tab character|\t|Tab")
print("This just shows the ^^^^tab charector in action")

# \\ : backslash
print("This is a backslash\\")
print("This just shows the ^^backslash in action")

# String Concatenation (adding two strings together to make one new string)

word = "words"
print("This has added a " + word + " to the sentence") 

# String Formatting (adding variables inside strings)

number = 10
print("This has added the number {} to the sentence".format(number)) # .format method {} is used to insert variables inside the string

# f-string (python 3.6 and above)
print(f"This has added the number {number} to the sentence") # f-string method f"" is used to insert variables inside the string

# input() function (to get user input)
user_input = input("Enter a string: ") # once you move past this line the info the user puts in will be stored in user_input variable (used user_input here but it could be anything name, place, time, etc....)
print("You entered: ", user_input) # I put in "James" as an example

# type() function (to get the type of a variable)
print("The type of user_input is: ", type(user_input))

# len() function (to get the length of a iriterable object) Iterables are strings, lists, tuples, dictionaries, sets, etc....
print("The length of user_input is: ", len(user_input))

# isinstance() function (to check if a variable is of a certain type)
print("Is user_input a string? ", isinstance(user_input, str))

# abs() function (to get the absolute value of a number) absolute value of a number can be positive or negative. Distance from zero is always positive but -5 is the absolute value of 5 because its 5 units from zero -5,-4,-3,-2,-1,0,1,2,3,4,5 are all absolute
print("The absolute value of -5 is: ", abs(-5))

# round() function (to round a number to a specified number of decimal places)
print("The rounded value of 3.145 is: ", round(3.145, 2)) # just because its 5 doesnt mean it should rounded to the next up - must round to the nearest decimal place. 3.145 is rounded to 3.15, but 3.41 will be rounded to 3.4

# sum() function (to get the sum of all the elements in a list)
print("The sum of all numbers in the list is: ", sum([1, 2, 14, 20, 5]))

# min() function (to get the smallest element in a list)
print("The smallest number in the list is: ", min([1, 2, 14, 20, 5]))

# max() function (to get the largest element in a list)
print("The largest number in the list is: ", max([1, 2, 14, 20, 5]))

# pow() function (to calculate the power of a number)
print("The power of 2 raised to the 3rd power is: ", pow(2, 3))

# divmod() function (to get the remainder of a division)
print("The remainder of 20 divided by 3 is: ", divmod(20, 3))

# Built-in Functions

# A
# abs() - returns the absolute value of a number
# aiter() - returns an iterator for an iterable
# all() - returns True if all elements of an iterable are true
# anext() - returns the next item from an iterator
# any() - returns True if any element of an iterable is true
# ascii() - returns a string containing a printable representation of an object

# B
# bin() - returns a string containing a printable representation of an integer in binary format
# bool() - returns a boolean value representing whether an object is true
# breakpoint() - enters the debugger at the call site
# bytearray() - returns a bytearray object
# bytes() - returns a bytes object

# C
# callable() - returns True if the object is callable
# chr() - returns a string representing a character with the given Unicode code point
# classmethod() - returns a class method for a function
# compile() - returns a code object from a string
# complex() - returns a complex number with the given real and imaginary parts

# D
# delattr() - deletes the attribute of an object
# dict() - returns a dictionary
# dir() - returns a list of all the attributes and methods of an object
# divmod() - returns the quotient and remainder of the division of two numbers

# E
# enumerate() - returns an iterator that produces tuples containing an index and value from an iterable
# eval() - evaluates a string as a Python expression and returns the result
# exec() - executes a string as a Python statement

# F
# filter() - returns an iterator yielding the items from the iterable for which the function returns true
# float() - returns a floating-point number with the given value
# format() - returns a formatted string
# frozenset() - returns a frozenset object

# G
# getattr() - returns the value of the named attribute of an object
# globals() - returns a dictionary representing the current global symbol table

# H
# hasattr() - returns True if the object has the specified attribute
# hash() - returns the hash value of an object
# help() - prints help information about an object or a module
# hex() - returns a string containing a printable representation of an integer in hexadecimal format

# I
# id() - returns the identity of an object
# input() - returns the input string as a number
# int() - returns an integer with the given value
# isinstance() - returns True if the object is an instance or subclass of the specified class
# issubclass() - returns True if the subclass is a subclass or the same class as the specified class
# iter() - returns an iterator for an iterable
# L
# len() - returns the number of items in an iterable
# list() - returns a list
# locals() - returns a dictionary representing the current local symbol table

# M
# map() - applies a given function to each item of an iterable and returns a list of the results
# max() - returns the largest item in an iterable
# memoryview() - returns a memory view object
# min() - returns the smallest item in an iterable

# N
# next() - returns the next item from an iterator

# O
# object() - returns a new object with the same class and attributes as the given object
# oct() - returns a string containing a printable representation of an integer in octal format
# open() - returns a file object
# ord() - returns the Unicode code point of a character

# P
# pow() - returns the power of a number
# print() - prints the objects to the standard output
# property() - returns a property object




# R
# range() - returns a sequence of numbers
# repr() - returns a string containing a printable representation of an object
# reversed() - returns a reverse iterator of an iterable
# round() - returns the rounded number of a given number

# S
# set() - returns a set
# setattr() - assigns the value of the named attribute of an object
# slice() - returns a slice object
# sorted() - returns a new sorted list from an iterable
# staticmethod() - returns a static method for a function
# str() - returns a string containing a printable representation of an object
# sum() - returns the sum of all the items in an iterable
# super() - returns a superclass object

# T
# tuple() - returns a tuple | Tuple is a sequence of immutable (unchangeable) objects | immutable means elements of a tuple cannot be changed after they are created | tuples are faster than lists and can be used as keys in dictionaries

# type() - returns the type of an object

# V
# vars() - returns a dictionary representing the current local or global symbol table

# Z
# zip() - returns an iterator that aggregates elements from each of the iterables

# _
# __import__() - imports a module | module is a file containing Python definitions and statements





