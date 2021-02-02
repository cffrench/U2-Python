import hello_world

import math 
import random
import copy

# use import to use hello_world.py

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
# can also use math.pow() (and other functions...)
print(math.pow(2, 5))

# user input
#fav_num = int(input("Enter your favorite number: "))
#print(fav_num, type(fav_num))

# conditionals
temperature = 37
if temperature > 32:
    print("It is warm outside")
else: 
    print("It is cold outside")
# use elif for else if

# loops
# while and for loops
# for (int i = 0; i < 5; i++) { }
# for item in sequence:
#   body
for i in range(5): # [0, 5) incrementing by 1
    print(i, end=" ") # default end is new line
print()

# warm up task
# e.g. 2, 4, ..., 38, 40
def print_even_numbers(stop=40):
    for i in range(2, stop, 2):
        print(i, end=", ")
    print(i + 2)

# functions 
# start with def
# they can accept keyword args
# call the function
print_even_numbers(stop=30)

# random numbers (import random)
# seed the generator for reproducibility
random.seed(0)
die_roll = random.randint(1, 6) # [1, 6]
print(die_roll)

# decimal formatting
# 3 ways to round to 2 decimal places
print(math.pi, round(math.pi, 2))
# C style
print("%.2f" %(math.pi))
# Pythonic
print("{:.2f}".format(math.pi))

# lists
# like arrays, but can grow/shrink in size
# lists are objects, they have methods
# <object>.<method>()
# can have mixed types
fibs = [1, 1, 2, 3, 5, 8]
print(fibs)
# use loops
# [0] [1]...
for value in fibs:
    print(value)
# use len() to get the number of items in the list
for i in range(len(fibs)):
    print(i, ":", fibs[i])

# built in functions
print(sum(fibs))
print(max(fibs))

# list methods
fibs.append(13)
print(fibs)

# nested lists
# we will use a nested list (e.g. 2D list) to store tabular data
matrix = [[0, 1, 2], [3, 4, 5]] # 2x3 table
print(matrix)

# task: define/call a pretty_print(table)
# prints the nested list in a nice grid structure
# 0 1 2
# 3 4 5

# python is pass by OBJECT REFERENCE
# object references are passed by value
# for more info and pics: https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/
def add_one(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] += 1

def clear_out(table):
    table = []
            
print("matrix before:", matrix)
add_one(matrix)
print("matrix after:", matrix)

print("matrix before:", matrix)
clear_out(matrix)
print("matrix after:", matrix)

# break! try the pretty_print(table)
def pretty_print(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j], end=" ")
        print()

pretty_print(matrix)

# shallow vs deep copy
matrix_copy = matrix.copy() # makes a shallow copy
# shallow copy: copies the references to objects, not
# the objects themselves
matrix_deep_copy = copy.deepcopy(matrix) # deep copy
# deep copy: copies the objects themselves

print("matrix before:", matrix)
print("matrix copy before:", matrix_copy)
print("matrix deep copy before:", matrix_deep_copy)
add_one(matrix)
print("matrix after:", matrix)
print("matrix copy after:", matrix_copy)
print("matrix deep copy after:", matrix_deep_copy)

# moral of the story: you probably want a deep copy

# file IO
# we want to load the contents of a csv file into a table (e.g. nested list)
# comma separated value file

def convert_to_numeric(values):
    # try to convert each value in values to a numeric type
    # skip over values that can't be converted
    for i in range(len(values)):
        try: 
            numeric_value = int(values[i])
            # success!
            values[i] = numeric_value
        except ValueError:
            print(values[i], "cannot be converted to an int")

def read_table(filename):
    table = []
    # 1. open
    infile = open(filename, "r")
    # 2. process (read/write)
    lines = infile.readlines()
    for line in lines:
        line = line.strip() # remove leading and trailing whitespace characters
        values = line.split(",") # split the string by comma into a list of strings
        convert_to_numeric(values)
        table.append(values)
    # need to convert "numeric values" to a numeric type
    # input example: int() float()
    print(lines)
    # 3. close
    infile.close()

    return table 

def write_table(filename, table):
    outfile = open(filename, "w")
    # TODO: challenge is to make sure you don't write an extra newline at the end
    for row in table:
        for i in range(len(row) - 1):
            outfile.write(str(row[i]) + ",")
        outfile.write(str(row[i + 1]) + "\n")

    outfile.close()


table = read_table("msrp.csv")
print(table)
write_table("msrp_copy.csv", table)

# classes 
# class: a collectiom of state (attributes) and behavior (methods)
# that completely describes something
# object: instance of a class

class Subject:
    """Represents a subject in a research study

    Attributes:
        sid(int): uniquely identifies a subject in the study
        name(str): name of the subject
        measurements(dict of str:float): measurements taken at a certain timestamp

        num_subjects(int): class-level attribute the tracks the total number 
            of subjects in the study
    """
    num_subjects = 0 # class-level attribute
    # meaning, one num_subjects variable is shared amongst all Subject objects

    # __init__() is a special method that initialized a new object
    # good practice is declare (and initialize) you instance-level methods there
    # self refers to the "current" AKA "invoking" object
    def __init__(self, name, measurements=None):
        self.sid = Subject.num_subjects # incrementing primary key
        Subject.num_subjects += 1
        self.name = name 
        if measurements is None:
            measurements = {}
        self.measurements = measurements

    # __str__() is a special method that is implicitly called
    # whenever a string representation of an object is needed
    def __str__(self):
        return "SID: " + str(self.sid) + " NAME: " + self.name + \
            " MEASUREMENTS: " + str(self.measurements)

    def record_measurement(self, timestamp, value):
        self.measurements[timestamp] = value 

# create some Subject objects!
spike = Subject("spike")
print(spike)

spike.record_measurement("2-2-21 10:11AM", 1.55)
print(spike)
print(spike.measurements)

gator = Subject("gary", measurements={})
print(gator)


