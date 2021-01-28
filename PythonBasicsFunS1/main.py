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

def read_table(filename):
    table = []
    # 1. open
    # 2. process
    # 3. close 
    infile = open(filename, "r") # "r" is for reading
    lines = infile.readlines()
    print(lines)
    # TODO: write a loop to iterate through each line
    # convert the numeric values to numeric types
    infile.close()

    return table

table = read_table("msrp.csv")
print(table)