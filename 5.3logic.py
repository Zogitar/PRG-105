# Area of shape finder


def main():
    print("This program will find the area of a shape for you.\n1. Rectangle\n2. Triangle\n3. Square\n4. Circle\n5. Quit")
    sele = input("Please enter the number of your selection:")
    if sele == '1':
        one()
    elif sele == '2':
        two()
    elif sele == '3':
        three()
    elif sele == '4':
        four()
    elif sele == '5':
        five()
    else:
        oth()


def oth():
    print("That is an invalid selection")
    sele = input("Please enter the number of your selection:")
    return sele


def one():
    wid = input("Enter the width of the rectangle in cm:")
    hei = input("Enter the height of the rectangle in cm:")
    reca = int(wid) * int(hei)
    print()
    print("the area of the rectangle is:", reca, "square cm")
    print()
    main()


def two():
    bas = input("Enter the base of the triangle in cm:")
    hei = input("Enter the height of the triangle in cm:")
    tria = int(bas) * int(hei) / 2
    print()
    print("the area of the triangle is:", tria, "square cm")
    print()
    main()


def three():
    sid = input("Please enter the length of one side of the square in cm:")
    squa = int(sid) * int(sid)
    print()
    print("the area of the square is:", squa, "square cm")
    print()
    main()


def four():
    rad = input("Please enter the length of the radius of the circle:")
    cira = int(rad) * int(rad) * 3.1415
    print()
    print("the area of the rectangle is:", format(cira, '.2f'), "square cm")
    print()
    main()


def five():
    print("Goodbye!")


main()
