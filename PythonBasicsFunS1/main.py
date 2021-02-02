import hello_world
# note: main() in hello_world.py will not execute
# because __name__ is not "__main__" (it is "hello_world")
import math
import random
import copy

# data types
# int, float, double, str, list, tuple, dict, set, etc.
x = 10
print(x, type(x))
x = "hello"
print(x, type(x))

# operators
# / floating point div
# // int div
# ** exponentiation
# can use the math module
print(math.pow(2, 5))

# user input
# fav_num = int(input("Enter your fav number: "))
# print(fav_num, type(fav_num))

# conditionals
temperature = 35
if temperature > 32:
    print("It is warm out")
else:
    print("It is cold out")
# note: use elif for else if

# loops
# while and for loops
# for (int i = 0; i < 5; i++) { }
# for item in sequence:
#   body
for i in range(5): # [0, 5) incrementing by 1
    print(i, end=" ") # default end is newline
print()

# range(start, stop): [start, stop)
# range(start, stop, step): [start, stop) incrementing by step

# warm up
# 2, 4, 6, ..., 40
def print_even_numbers(stop=40):
    for i in range(2, stop, 2):
        print(i, end=", ")
    print(i + 2)

# functions 
# they start with def
# and they can accept keyword arguments
print_even_numbers(stop=20) # call

# random numbers (import random)
random.seed(0) # for reproducibility
die_roll = random.randint(1, 6) # [1, 6]
print(die_roll)

# decimal printing
# we can use round(value, 2)
print(math.pi, round(math.pi, 2))
# C style
print("%.2f" %(math.pi))
# Pythonic style
print("{:.2f}".format(math.pi))

# lists
# like are like arrays...
# but they can grow/shrink in size
# they are objects (methods)
# recall: <object>.<method>()
# they can have mixed types
fibs = [1, 1, 2, 3, 5, 8]
print(fibs)
for value in fibs:
    print(value)
# indices
for i in range(len(fibs)):
    print(i, ":", fibs[i])

# built in list functions
# len()
print(sum(fibs))
print(max(fibs))

# list methods
fibs.append(13)
print(fibs)
print(fibs[-1])

def add_one(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] += 1

def clear_out(table):
    table = []

# python is pass by OBJECT REFERENCE
# object references are passed by value
# for more info: https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/
# nested list (2D list, table)
matrix = [[0, 1, 2], [3, 4, 5]]
print(matrix)
print("matrix before:", matrix)
add_one(matrix) # the reference to matrix is passed by value
# (it is copied) into the parameter table
print("matrix after:", matrix)

print("matrix before:", matrix)
clear_out(matrix)
print("matrix after:", matrix)

# task: define/call a pretty_print(table)
# accept a 2D list
# print in a grid structure
# 0 1 2
# 3 4 5

def pretty_print(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j], end=" ")
        print()

pretty_print(matrix)

# shallow vs deep copy
matrix_copy = matrix.copy() # shallow copy
# shallow copy: object references are copied, not the objects themselves
matrix_deep_copy = copy.deepcopy(matrix)
# deep copy: objects are copied
print("matrix before:", matrix)
print("matrix copy before:", matrix_copy)
print("matrix deep copy before:", matrix_deep_copy)
add_one(matrix)
print("matrix after:", matrix)
print("matrix copy after:", matrix_copy)
print("matrix deep copy after:", matrix_deep_copy)
# moral of the story: you probably want a deep copy

# file IO
# we want to open a csv file and store its contents
# in a nested list (e.g. table)
# csv file: comma separated value file

def convert_to_numeric(values):
    # attempt to convert each value in the 1D list values to a numeric type
    # if it values, skip the value
    for i in range(len(values)):
        try:
            numeric_value = int(values[i])
            # success!!
            values[i] = numeric_value
        except ValueError:
            # failure
            print(values[i], "could not be converted a numeric type")

def read_table(filename):
    table = []
    # 1. open
    # 2. process
    # 3. close 
    infile = open(filename, "r") # "r" is for reading
    lines = infile.readlines()
    print(lines)
    for line in lines:
        # get rid of the newline character at the end of the line
        line = line.strip() # remove leading and trailing whitespaces
        # split the line into its individual values
        values = line.split(",")
        convert_to_numeric(values)
        table.append(values)
    # TODO: write a loop to iterate through each line
    # convert the numeric values to numeric types
    infile.close()

    return table

def write_table(filename, table):
    # TODO: challenge: get rid of the extra
    # newline that is written out
    outfile = open(filename, "w")
    for row in table:
        for i in range(len(row) - 1):
            outfile.write(str(row[i]) + ",")
        outfile.write(str(row[i + 1]) + "\n")
    outfile.close()

table = read_table("msrp.csv")
print(table)
write_table("msrp_copy.csv", table)

# classes 
# class: a collection of state (attributes) and behavior (methods)
# that completely describes something
# object: an instance of a class

class Subject:
    """Represents a subject in a research study.

    Attributes:
        sid(int): a unique value that identifies each subject
        name(str): name of the subject
        measurements(dict of string:float): records study measurements for each subject

        num_subjects(int): class-level attribute that keeps track of the total number of subjects

    """
    num_subjects = 0 # this is a class-level attribute!!
    # means one num_subjects variable is shared amongst all subject objects
    # DO NOT put your instance-level variable declarations here!!

    # special method __init__()
    # initializer for new Subject objects (e.g. constructor)
    # self is like this
    # and refers to the "current" or "invoking" object
    def __init__(self, name, measurements=None):
        # declare and initialize instance-level attributes
        self.sid = Subject.num_subjects
        Subject.num_subjects += 1
        self.name = name 
        if measurements is None:
            measurements = {}
        self.measurements = measurements

    # special method __str__() that is invoked anytime
    # a string representation of an object is needed
    def __str__(self):
        return "SID: " + str(self.sid) + " NAME: " + self.name + \
            " MEASUREMENTS: " + str(self.measurements)

    def record_measurement(self, timestamp, value):
        # probably should some error checking...
        self.measurements[timestamp] = value 

gooeyduck = Subject("gooeyduck")
print(gooeyduck)

gooeyduck.record_measurement("2-2-21 8:50AM", 1.55)
print(gooeyduck)
print(gooeyduck.measurements)

# GS: note after class changing order to make sure spike's measurements are empty
spike = Subject("spike")
print(spike)
