# 6.2 Reading Files Coding


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


main()
