import random

print()


PI = 3.14159265358979

# format specifiers
print("%20.5f %20.8f\n" %(PI, PI))  

# input
name = input("Enter your name: ")
x = int(input("Enter an integer: "))  # input() reads in the data as a String, so cast it
print("Thank you " + name + ". Half of that is: %d" %(x / 2))

# conditionals
if (x > 200):
    print ("Your input number is greater than 200")
elif (100 < x <= 200):
    print ("Your input > 100 but <= 200")
else:
    print ("Your input number is <= 100")

# use natural language for not, and, or
if x % 25 == 0 or (x % 99 == 0 and x > 0):
    print("Woot! special number!")

# checking membership (works for strings, lists, other listy shit like that)
st = "Hello, World!"
if name in st:
    print("yes: '" + name + "' is in '" + st + "'\n")
else:
    print("nope: '" + name + "' is not in '" + st + "'\n")

# loops
sum = 0
for i in range (1, 11, 1):
    sum += i
    print ("i =", i, "\t total=", sum)

print()
for ch in "foobar":
    print(ch + "-", end="")

print("\n")
sum = 0
temp = 0
while (temp >= 0):
    temp = int(input("Enter a non-negative integer (negative to end this loop): "))
    if (temp >= 0):
        sum += temp

print ("Total of your input:", sum)









print()