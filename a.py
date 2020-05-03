# author: Cody N.S. |  project: "Back to Basics"

import random


# functions
def multiply(first, second):
    return first * second



# -----------------------------------------------------------------------------
def main():  

    print()
    PI = 3.14159265358979

    # format specifiers
    print("%20.5f %20.8f\n" %(PI, PI))  


    # input
    name = input("Enter your name: ")
    x = int(input("Enter an integer: "))  # input() reads in the data as a String, so cast it
    print("\nThank you " + name + ". Half your input number is:", (x // 2)) # // for int div


    # conditionals
    if x > 200:
        print ("Your input number is greater than 200")
    elif 100 < x <= 200:  # awesome that Pyhon can parse this
        print ("Your input is > 100 but <= 200")
    else:
        print ("Your input number is <= 100")


    # use natural language for not, and, or
    if x % 25 == 0 or (x % 99 == 0 and x > 0):
        print("Woot! Special number!")


    # checking membership (works for strings, lists, other listy shit like that)
    print ("Your name '" + name + "' is ", end="")
    st = "Hello, World!"
    if not name in st:
        print ("not ", end="")
    print ("in '" + st + "'\n")


    # loops
    sum = 0
    for i in range (1, 11, 1):
        sum += i
        print ("i =", i, "\t total =", sum)

    print()
    for ch in "foobar":
        print(ch + "-", end="")

    print("\n")
    sum = 0
    temp = 0
    while (temp >= 0):
        temp = int(input("Enter a non-negative integer (negative to end the calculation): "))
        if (temp >= 0):
            sum += temp

    print ("\n  Final total:", sum)


    # functions (see top for definitions)
    product = multiply(5, 6)
    print("\nResult of 5 x 6 is:", product)





    print() 
# -----------------------------------------------------------------------------

# run this entire thing
main()