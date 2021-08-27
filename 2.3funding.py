print("This program will calculate how much you are spending on each monthly expense and how much will be remaining afterwards.")
i = input("What is your total monthly income?")
In = int(i)
h = input("How much do you spend on housing each month?")
H = int(h)
f = input("How much do you spend on food each month?")
F = int(f)
t = input("How much do you spend on transportation each month?")
T = int(t)
p = input("How much do you spend on your phone each month?")
P = int(p)
u = input("How much do you spend on utilities each month?")
U = int(u)
c = input("How much do you spend on clothes each month?")
C = int(c)
print("")

p1 = H/In
p2 = F/In
p3 = T/In
p4 = P/In
p5 = U/In
p6 = C/In
p7 = In-H-F-T-P-U-C


print(format(p1, '%'), " of your income is spent on housing monthly.")
print(format(p2, '%'), " of your income is spent on food monthly.")
print(format(p3, '%'), " of your income is spent on transportation monthly.")
print(format(p4, '%'), " of your income is spent on phone's monthly.")
print(format(p5, '%'), " of your income is spent on utilities monthly.")
print(format(p6, '%'), " of your income is spent on clothes monthly.")
print("You have $", p7, "remaining.")
