# User defined Functions

# They give us repeatable power
# We can define a function with a name, parameters, and a body
# Syntax: def function_name(parameters):
# def tells python we are about to define a function
# after the : next line we tab over

# now you have a code block
def greet_user(name):
    print("Hello, ", name)

# after defining the function, we can call it
greet_user("John Doe") # will print "Hello, John Doe"
greet_user("Jane Doe") # will print "Hello, Jane Doe"
greet_user("Alice Doe") # will print "Hello, Alice Doe"

def divi():
    print("="*50)

divi()


# Returning values from a function
def aye():
    return "Aye, Captain!"


print(aye()) # will print "Aye, Captain!"

# functions with parameters
# estabilish a required verable of value for the function to operate

def personal_greating(name): #creating a function that takes a name as a parameter - now i dont have to do the intire f-string
    print(f"Hello, {name}, welcome to user defined functions!!")

# read from top to bottom
personal_greating("James") # will print "Hello, John Doe, welcome to user defined functions!!"
personal_greating("Jane") # will print "Hello, Jane Doe, welcome to user defined functions!!

# more complex example

def class_info(instructor, students, course_name, course_student_count=None):
    """Prints instructor, course name, and student information."""

    print(f"The instructor is {instructor}, the course name is {course_name}, and the course has {len(students)} students in it.")

    if course_student_count and course_student_count != len(students):
        print(f"WARNING: Provided student count ({course_student_count}) does not match actual count ({len(students)}).")

students_152 = ["John Doe", "Jane Doe", "Alice Doe", "Bob Doe", "Charlett Dow", 
    "David Smith", "Emily Johnson", "Frank Wilson", "Grace Thompson", 
    "Henry Brown", "Isabella Clark", "Jack Wilson"]

class_info("Mr. Smith", students_152, "Introduction to Python") 





