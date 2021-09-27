# 6.3 Try and Except statements Coding


def main():
    totals = open("sales_total.txt", "r")
    counter = 0
    total = 0
    for line in totals:
        print(line)
        counter += 1
        total += float(line.rstrip('n'))
    print("Total:", total)
    print("Number of entries:" + str(counter))
    print("Average total:", format(total/counter, '.2f'))


try:
    main()
except ValueError:
    print("That value is not valid.")
try:
    filetest = open("sales_total.txt", "r")
    filetest.close()
except IOError:
    print("That file doesn't exist.")
try:
    fail = open("frenchbread.txt", "r")
    fail.close()
except IOError:
    print("That file doesn't exist.")
