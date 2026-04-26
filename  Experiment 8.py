my_dict = {'a': 3, 'b': 1, 'c': 2}

# Ascending (small to large)
asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))

# Descending (large to small)
desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

print("Ascending:", asc)
print("Descending:", desc)

#Check if a Key Exists in a Dictionary

my_dict = {'a': 10, 'b': 20, 'c': 30}

# Input key from user
key = input("Enter key to check: ")

# Check if key exists
if key in my_dict:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")
    
#Merge Two Python Dictionaries

# First dictionary
dict1 = {'a': 1, 'b': 2}

# Second dictionary
dict2 = {'c': 3, 'd': 4}

# Merging dictionaries
merged_dict = {**dict1, **dict2}

# Output
print("Merged Dictionary:", merged_dict)

#Add an Item in a Tuple

# Original tuple
t = (1, 2, 3)

# Adding item (tuples are immutable, so create new tuple)
t = t + (4,)
print("Updated Tuple:", t)

#Create a Tuple with Different Data Types

t = (10, 3.14, "Hello", True)

# Output
print("Tuple:", t)

#Sum All Items in a List

# List of numbers
lst = [10, 20, 30, 40]

# Sum of list
total = sum(lst)

# Output
print("Sum of list:", total)

#Get the Largest Number from a List

# List of numbers
lst = [10, 45, 23, 67, 12]

# Find largest number
largest = max(lst)

# Output
print("Largest number:", largest)

#Add Member(s) in a Set

# Create a set
s = {1, 2, 3}

# Add single element
s.add(4)

# Add multiple elements
s.update([5, 6])

# Output
print("Updated Set:", s)

#Reverse the Order of Items in an Array

# Import array module
import array

# Create an array
arr = array.array('i', [1, 2, 3, 4, 5])

# Reverse the array
arr.reverse()

# Output
print("Reversed array:", arr)

#Create an Array and Access Elements Using Index

# Import array module
import array

# Create an array of 5 integers
arr = array.array('i', [10, 20, 30, 40, 50])

# Display all elements
print("Array elements:", arr)

# Access elements using index
print("First element:", arr[0])
print("Second element:", arr[1])
print("Third element:", arr[2])
print("Fourth element:", arr[3])
print("Fifth element:", arr[4])