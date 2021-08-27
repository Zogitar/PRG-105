print("=" * 10, "Section 2.3 string output", "=" * 10)
print("Xander Welch")
print("IT \n")

print("=" * 10, "Section 2.3 using quotes", "=" * 10)
print('The dog says "woof!"\n')

print("=" * 10, "Section 2.4 printing variable values", "=" * 10)
x = 19
y = "Xander"
print(x)
print("age", x)
i = 42
print("age", i)
print("")

print("=" * 10, "Section 2.6 keyboard input", "=" * 10)
name = input("What is your name?")
print("Hello,", name)
print("")

print("=" * 10, "Section 2.6-2.7 numeric input and calculations", "=" * 10)
age = input("How old are you?")
num_age = int(age)
print("This year you are", age)
print("Next year you will be", (num_age+1))
print("")

print("=" * 10, "Section 2.7 performing calculations", "=" * 10)
answer = 7/2
print("7/2=", answer)
remainder = 7 % 2
print("The remainder of 7/2 is", remainder)
print("")

print("=" * 10, "Section 2.7 data conversion", "=" * 10)
print("2 + 2 = " + str(2 + 2))
print("2 / 2 = " + str(2 / 2))
h = 1+2
p = 3-2
print("3/1=", (h/p))
print("9/3=", (9/h))

print("=" * 10, "Section 2.8 print statement options", "=" * 10)
print('one', end='-')
print('two', end='-')
print('three\n')

print("=" * 10, "Section 2.8 escape codes", "=" * 10)
print("Sunday    Monday     Tuesday     Wednesday    Thursday    Friday     Saturday\n")

print("=" * 10, "Section 2.8 concatenating strings", "=" * 10)
nam = input("What is your name?")
print("Hello,", nam)
print("")

print("=" * 10, "Section 2.8 formatting numbers", "=" * 10)
number = 6548974897.5687979797
print("$"+format(number, '30,.2f'))
print("")

print("=" * 10, "Section 2.8 formatting a percentage", "=" * 10)
percentage = .02
print(format(percentage, '%'))
