# different types of parameters

# basic parameteres assume value from arguments passed into the defined functioin when its called

def name_parameter(first,middle, last):
    print(f"Hello, {first} {middle} {last}!")

# positional arguments : the postion of argument determine which parameter it becomes the value of
name_parameter("James", "Earl", "Sanders") # will print "Hello, James Earl Sanders!" first > second > third parameters
name_parameter("Sanders", "James", "Earl") 

# keyword arguments : arguments are passed as a name-value pair, where the name is the parameter name
# explicitly state which parameter states which value

name_parameter(last="Sanders", first="James", middle="Earl") 

print("="*50)


# default arguments : if no value is provided for a parameter, it will default to the provided value
def greeting(name="World"):
    print(f"Hello, {name}!")

greeting() # will print "Hello, World!"
greeting("James") # will print "Hello, James!"

print("="*50)

# *args : allows a function to accept any number of positional arguments | unkknown number of arguments, brought into the functions as a tuple 

def vet_hands(staff, *vols):
    print(f"On staff today we have {staff[0]} and {staff[1]}")
    if vols:
        print("They will be assisted by the follwoing volunteers:")
        for vol in vols:
            print(vol)

vet_hands(["Dr. Samantha Johnson", "Dr. Michael Thompson"], "Dylan", "Grace", "Josh", "Walter", "Phillip")

print("="*50)
# **kwargs : allows a function to accept any number of keyword arguments | brought into the functions as a dictionary

def routine(**daily_events):
    print(daily_events)

routine(morning="I wake up, brush my teeth, eat breakfast", mid_morning="I walk my dog",afternoon="Grading and preping for class", evening="I'm in class", night="I sleep") 






