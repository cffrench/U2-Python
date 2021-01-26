import hello_world
# note: main() in hello_world.py will not execute
# because __name__ is not "__main__" (it is "hello_world")
import math

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
fav_num = int(input("Enter your fav number: "))
print(fav_num, type(fav_num))

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
