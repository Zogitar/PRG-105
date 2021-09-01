# chapter 3 exercises:
print("=" * 10, "Section 3.1 relational operators", "=" * 10)
a = 6
b = 8
c = 5
print(9 > a)
if a == b:
    print("(a=b)")
if a != b:
    print("(a≠b)")
if a > b:
    print("(a>b)\n")
if a < b:
    print("(a<b)\n")

print("=" * 10, "Section 3.2 if-else", "=" * 10)
age = int(input("How old are you? "))
if age > 17:
    print("You are old enough to vote\n")
else:
    print("You are not old enough to vote\n")

print("=" * 10, "Section 3.3 comparing strings", "=" * 10)
user_password = input("Please enter the password: ")
if user_password == "narwhals":
    print("that is correct\n")
else:
    print("that is not correct\n")

print("=" * 10, "Section 3.4 if-elif-else", "=" * 10)
number = int(input("Please enter a number between 1 and 5: "))
if number >= 6:
    print("That is not a valid number\n")
elif number >= 5:
    print("V\n")
elif number >= 4:
    print("IV\n")
elif number >= 3:
    print("III\n")
elif number >= 2:
    print("II\n")
elif number >= 1:
    print("I\n")

print("=" * 10, "Section 3.5 multiple conditions", "=" * 10)
customer_age = int(input("How old is the customer? "))
cost = 0
if customer_age >= 62:
    cost = 9.89
elif customer_age >= 12:
    cost = 12.89
elif customer_age >= 4:
    cost = .99
elif customer_age < 4:
    cost = 0.00
print("Your cost for a customer who is " + str(customer_age) + " years old")
print("is $" + format(cost, ",.2f"))
print("")

print("=" * 10, "Section 3.5 logical operators", "=" * 10)
d = 10
e = 10
f = 12
if d == 10 and e == 10:
    print("true")
else:
    print("false")
if d == 10 or f == 10:
    print("true")
else:
    print("false")
if f:
    print("true\n")
if not f:
    print("false\n")

print("=" * 10, "Section 3.6 boolean variables", "=" * 10)
tired = True
hungry = False
if tired and not hungry:
    print("Eyes close")
else:
    print("Eyes open")
if hungry:
    print("Baby cries")
else:
    print("Baby is silent")
