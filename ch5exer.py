# Chapter 5 Exercises
import math
from random import randint
for _ in range(10):
    rnum = randint(1, 10)
print("=" * 10, "Section 5.2 call an existing function", "=" * 10)


def hello():
    print("Hello Sweetie!")


hello()
print()
print("=" * 10, "Section 5.2 create and call an existing function", "=" * 10)


def joke():
    print("So a cop saw a car with three old women driving down the highway at 20 miles per hour, he pulled them over and asked them why they were driving so slow. He quickly found out they were following the highway sign and not the speed limit sign as they were on highway 20, he then noticed the women in the back with terrified looks on their faces, he asked the driver if they were alright, to which she replied, well, we just came off of highway 160.")


joke()
print()
print("=" * 10, "Section 5.3 design a program using functions", "=" * 10)


def main():
    line1()
    line2()
    line3()
    line4()
    line5()


def line1():
    print("Knock knock")


def line2():
    print("Who's there?")


def line3():
    print("Dini")


def line4():
    print("Dini who?")


def line5():
    print("No, its not Dinihou, its Houdini")


main()
print()
print("=" * 10, "Section 5.4 using local variables", "=" * 10)


def main2():
    name = "Ben Chang"
    print("Hello", name)
    get_name()


def get_name():
    name = input("What is your name?")
    print("Hello", name)


main2()
print()
print("=" * 10, "Section 5.5 passing arguments", "=" * 10)


def main3():
    my_number = 7
    square(my_number)


def square(value):
    squared_value = value * value
    print(squared_value)


main3()
print()
print("=" * 10, "Section 5.5 passing multiple arguments", "=" * 10)


def main4():
    num_one = 5
    num_two = 7
    add(num_one, num_two)


def add(one, two):
    total = one + two
    print(total)


main4()
print()
print("=" * 10, "Section 5.7 value returning functions", "=" * 10)
PI = 3.14


def main5():
    r = rnum
    r2 = r * r
    area(r2)


def area(radius_squared):
    my_area = radius_squared * PI
    print(format(my_area, ",.2f"))


main5()
print()
print("=" * 10, "Section 5.8 value returning functions", "=" * 10)


def main6():
    print("This program will calculate your BMI")
    height = float(input("What is your height in inches?"))
    weight = float(input("What is your weight in pounds?"))
    variable = bmi(height, weight)

    print(format(variable, '.1f'))


def bmi(height_inches, weight_pounds):
    # BMI = (Weight in Pounds / (Height in inches x Height in inches)) x 703
    patient_bmi = (weight_pounds / (height_inches * height_inches)) * 703
    return patient_bmi


main6()
print()
print("=" * 10, "Section 5.9 use the math module", "=" * 10)
number_to_round = 4.243


def roundup():
    print(math.ceil(number_to_round))


roundup()
