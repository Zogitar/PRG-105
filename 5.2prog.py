# Number between 20 and 100 divisibility code


def main():
    var = int(input("Enter a whole number between 20 and 100:"))
    cor = validate(var)
    two = divbtw(cor)
    three = divbth(cor)
    five = divbf(cor)
    out(cor, two, three, five)


def validate(var):
    if 20 <= var <= 100:
        return var
    else:
        while var < 20 or var > 100:
            print("That is an invalid value.")
            var = int(input("Enter a whole number between 20 and 100:"))
        return var


def divbtw(cor):
    if cor % 2 == 0:
        return " is divisible by 2"
    else:
        return " is not divisible by 2"


def divbth(cor):
    if cor % 3 == 0:
        return " is divisible by 3"
    else:
        return " is not divisible by 3"


def divbf(cor):
    if cor % 4 == 0:
        return " is divisible by 4"
    else:
        return " is not divisible by 4"


def out(num, twod, threed, fived):
    print(str(num) + twod)
    print(str(num) + threed)
    print(str(num) + fived)


main()
