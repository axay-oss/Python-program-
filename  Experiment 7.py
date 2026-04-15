#1)Tuple creation and basic operations

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Length
print("Length of tuple:", len(t1))

# Concatenation
print("Concatenation:", t1 + t2)

# Repetition
print("Repetition:", t1 * 2)

# Membership
print(2 in t1)
print(10 not in t1)

#2)Indexing, negative indexing, slicing, iteration

t = (10, 20, 30, 40, 50)

# Indexing
print("First element:", t[0])
print("Third element:", t[2])

# Negative Indexing
print("Last element:", t[-1])
print("Second last:", t[-2])

# Slicing
print("Elements 1 to 3:", t[1:4])
print("First three:", t[:3])
print("Last three:", t[-3:])

# Iteration
print("Tuple elements:")
for i in t:
    print(i)
    
#3)Tuple immutability and deletion

t = (1, 2, 3, 4)

# Tuples are immutable
# t[1] = 10   # This will give an error

print("Original tuple:", t)

# Deleting tuple
del t
# print(t)   # This will give an error because tuple is deleted

#4)Built-in tuple functions

seq = [5, 2, 8, 1, 9]

t = tuple(seq)

print("Tuple:", t)

print("Length:", len(t))
print("Maximum:", max(t))
print("Minimum:", min(t))