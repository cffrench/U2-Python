# this is a one line comment

""" 
this is
a 
multi line 
comment 
"""

# there are two ways to run a python file (AKA module)
# 1. directly: e.g. python hello_world.py
# __name__ that when a module is run directly stores "__main__"
# 2. by importing the module from another module
# e.g. main.py: import hello_world
# __name__ in hello_world will store "hello_world"

def main():
    print("hello CPSC 322")

if __name__ == "__main__":
    # run a main function or similar
    main()
