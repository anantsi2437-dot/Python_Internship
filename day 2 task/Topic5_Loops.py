# Numbers 1 to 20
for i in range(1, 21):
    print(i)

# Even Numbers
for i in range(2, 51, 2):
    print(i)

# Odd Numbers
for i in range(1, 51, 2):
    print(i)

# Multiplication Table
num = int(input("Enter Number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Sum of First N Natural Numbers
n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)
