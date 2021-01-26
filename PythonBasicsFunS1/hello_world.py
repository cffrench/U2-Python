# this is a one line comment 

""" 
this is
a multi
line comment
"""

# two ways to run a python file (AKA module)
# 1. directly: e.g. python hello_world.py
# __name__ == "__main__"
# 2. by importing the module from another module
# example: main.py: import hello_world
# in hello_world.py __name__ == "hello_world"

def main():
    print("hello CPSC 322!!")

if __name__ == "__main__":
    main()