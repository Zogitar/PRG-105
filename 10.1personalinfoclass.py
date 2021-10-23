# Personal Information Class coding

class P:
    def __init__(self, name, address, age, phonenum):
        self.__namev = name
        self.__addressv = address
        self.__agev = age
        self.__phonenumv = phonenum

    def set_namev(self, name):
        self.__namev = name

    def set_addressv(self, address):
        self.__addressv = address

    def set_agev(self, age):
        self.__agev = age

    def set_phonenumv(self, phonenum):
        self.__phonenumv = phonenum

    def get_namev(self):
        return self.__namev

    def get_addressv(self):
        return self.__addressv

    def get_agev(self):
        return self.__agev

    def get_phonenumv(self):
        return self.__phonenumv

    def __str__(self):
        return 'Name: ' + self.__namev + "\nAddress: " + self.__addressv + "\nAge: " + self.__agev + "\nPhone Number: " + self.__phonenumv


def main():
    me = P("Xander", "3104 Oak Terrace, Island Lake", "19", "379-107-6382\n")
    family = P("Delia", "3104 Oak Terrace, Island Lake", "53", "379-156-8923\n")
    friend = P("Cody", "4591 Droke Avenue, McHenry", "17", "739-127-9758\n")
    print(me)
    print(family)
    print(friend)


main()
