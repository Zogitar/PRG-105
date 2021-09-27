# 6.1 File Programing


def main():
    usco = int(input("How many people do you want to add to the file?"))
    info = open("info.txt", "w")
    for people in range(0, usco):
        name = input("What is the persons name?")
        numb = input("What is the persons phone number?")
        email = input("What is the persons email address?")
        info.write(name + "," + numb + "," + email + "\n")
    info.close()


main()

