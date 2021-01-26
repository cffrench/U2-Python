import hello_world

import math 

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