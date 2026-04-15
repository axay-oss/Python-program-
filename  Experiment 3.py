# Greatest of 3 Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Greatest is:", a)
elif b > c:
    print("Greatest is:", b)
else:
    print("Greatest is:", c)

# Odd or Even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Uppercase or Lowercase
ch = input("Enter a character: ")

if ch.isalpha():
    if ch.isupper():
        print("Uppercase Letter")
    else:
        print("Lowercase Letter")
else:
    print("Not an alphabet")

# Number or Character
x = input("Enter something: ")

if x.isdigit():
    print("It is a Number")
elif x.isalpha():
    print("It is a Character/String")
else:
    print("It is a Special Character")