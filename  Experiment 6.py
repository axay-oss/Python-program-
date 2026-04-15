#1) Membership operators (in, not in)
my_list = [10, 20, 30, 40, 50]

num = int(input("Enter a number to check: "))

if num in my_list:
    print("Element is present in the list")
else:
    print("Element is NOT present in the list")

if num not in my_list:
    print("Element is not in the list")
    
# 2) Indexing, negative indexing, and slicing
my_list = [1, 2, 3, 4, 5, 6]

print("List:", my_list)

# Indexing
print("First element:", my_list[0])
print("Third element:", my_list[2])

# Negative Indexing
print("Last element:", my_list[-1])
print("Second last element:", my_list[-2])

# Slicing
print("Elements from index 1 to 4:", my_list[1:5])
print("First three elements:", my_list[:3])
print("Last three elements:", my_list[-3:])

#3) Update, append, insert, delete
my_list = [10, 20, 30, 40]

# Update
my_list[1] = 25
print("After update:", my_list)

# Append
my_list.append(50)
print("After append:", my_list)

# Insert
my_list.insert(2, 35)
print("After insert:", my_list)

# Delete using remove()
my_list.remove(30)
print("After remove:", my_list)

# Delete using pop()
my_list.pop()
print("After pop:", my_list)

#4)Basic list operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
print("Concatenation:", list1 + list2)

# Repetition
print("Repetition:", list1 * 2)

# Length
print("Length of list1:", len(list1))

# Maximum and Minimum
print("Maximum:", max(list1))
print("Minimum:", min(list1))