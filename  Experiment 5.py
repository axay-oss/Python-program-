#1. WAP to calculate length of string

str1 = input("Enter a string: ")
length = len(str1)
print("Length of string is:", length)

#2. WAP to make string from first 2 and last 2 characters

str1 = input("Enter a string: ")

if len(str1) < 2:
    print("String is too short")
else:
    result = str1[:2] + str1[-2:]
    print("New string:", result)
    
#3. WAP to concatenate two strings

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = str1 + str2
print("Concatenated string:", result)