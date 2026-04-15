# Display Even Numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Add Odd Numbers from 1 to 10
sum = 0

for i in range(1, 11):
    if i % 2 != 0:
        sum += i

print("Sum of odd numbers:", sum)


# Fibonacci Series (0 to 50)
a = 0
b = 1

print("Fibonacci series:")

while a <= 50:
    print(a)
    c = a + b
    a = b
    b = c


# Remove Characters with Odd Index
s = input("Enter a string: ")

result = ""

for i in range(len(s)):
    if i % 2 == 0:
        result += s[i]

print("Result:", result)