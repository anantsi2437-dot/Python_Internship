# Even or Odd
num = int(input("Enter Number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Voting Eligibility
age = int(input("Enter Age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")

# Greater Among Two Numbers
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

if a > b:
    print("Greater =", a)
else:
    print("Greater =", b)

# Largest Among Three Numbers
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

print("Largest =", max(a, b, c))

# Pass or Fail
marks = float(input("Enter Marks: "))

if marks >= 33:
    print("Pass")
else:
    print("Fail")