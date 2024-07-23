# typecasting means changing the data type of a variable.

# int() function (to convert a string to an integer)
print("The integer value of '10' is: ", int('10')) # entereed as a string to convert to integer

# str() function (to convert a number to a string)
print("The string value of 10 is: ", str(10)) # entereed as a number to convert to string

# float() function (to convert a string to a float)
print("The float value of '10.5' is: ", float('10.5')) # entereed as a string to convert to float

# bool() function (to convert a value to a boolean value [true or false]) | 0 or anything empty will be considered false
print("The boolean value of 10 is: ", bool(10)) 
print("The boolean value of 0 is: ", bool(0)) # anything thats 0 is considered false any other number is considered true 
print(bool([])) # empty list is considered false 
print(bool(-1)) # negative number is considered true anything other then 0 is considered true even negative numbers 
print("The boolean value of 'True' is: ", bool('True'))
print("The boolean value of 'False' is: ", bool('False'))
print("The boolean value of '' is: ", bool(''))