# This is a sample Python script.
stu = 5
vet = 7
ss = 2
ret = 6
gen = 10
some = .9
many = .85
lots = .8
print("Ticket Prices Based On Customer:\n1.student: $5.00\n2.Veteran: $7.00\n3.Show Sponsor: $2.00\n4.Retiree: $6.00\n5.General public: $10.00\n\nDiscounts:\nPeople buying 4 - 8 tickets get a 10% discount.\nPeople buying 9-15 tickets get a 15% discount.\nPeople buying more than 15 tickets get a 20% discount.\n")
cus = int(input("What category of customer do you fit into? (enter 1-5)"))
num = int(input("How many tickets will you be purchasing?"))
if cus == 1 and num >= 15:
    print("$", format(stu*num*lots, '.2f'))
elif cus == 1 and num >= 9:
    print("$", format(stu*num*many, '.2f'))
elif cus == 1 and num >= 4:
    print("$", format(stu*num*some, '.2f'))
elif cus == 1 and num >= 1:
    print("$", format(stu*num, '.2f'))
if cus == 2 and num >= 15:
    print("$", format(vet*num*lots, '.2f'))
elif cus == 2 and num >= 9:
    print("$", format(vet*num*many, '.2f'))
elif cus == 2 and num >= 4:
    print("$", format(vet*num*some, '.2f'))
elif cus == 2 and num >= 1:
    print("$", format(vet*num, '.2f'))
if cus == 3 and num >= 15:
    print("$", format(ss*num*lots, '.2f'))
elif cus == 3 and num >= 9:
    print("$", format(ss*num*many, '.2f'))
elif cus == 3 and num >= 4:
    print("$", format(ss*num*some, '.2f'))
elif cus == 3 and num >= 1:
    print("$", format(ss*num, '.2f'))
if cus == 4 and num >= 15:
    print("$", format(ret*num*lots, '.2f'))
elif cus == 4 and num >= 9:
    print("$", format(ret*num*many, '.2f'))
elif cus == 4 and num >= 4:
    print("$", format(ret*num*some, '.2f'))
elif cus == 4 and num >= 1:
    print("$", format(ret*num, '.2f'))
if cus == 5 and num >= 15:
    print("$", format(gen*num*lots, '.2f'))
elif cus == 5 and num >= 9:
    print("$", format(gen*num*many, '.2f'))
elif cus == 5 and num >= 4:
    print("$", format(gen*num*some, '.2f'))
elif cus == 5 and num >= 1:
    print("$", format(gen*num, '.2f'))
