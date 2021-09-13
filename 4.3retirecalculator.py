# Retirement savings calculator code:
age = int(input("How old are you currently?"))
goag = int(input("What age do you plan to retire at?"))
yein = int(input("What is your current yearly income?"))
insa = int(input("What percent of your income do you save?"))/100
tots = int(input("How much money do you currently have in your savings?"))
savco = yein*insa
stop = 1
print("This projection assumes a 3% raise each year and a 6% yearly return on investment. The first line wil be your current status.")
print("Year           Income            Savings Contribution         Total Savings")
while stop and not 0:
    print(age, "           ", format(yein, '.2f'), "          ", format(savco, '.2f'), "                      ", format(tots, '.2f'))
    if age == goag:
        stop = 0
    yein = yein*1.03
    savco = yein*insa
    tots = (tots + savco)
    age += 1
