# Sales Calculator:
sun = input("What were the total sales on Sunday?")
mon = input("What were the total sales on Monday?")
tue = input("What were the total sales on Tuesday?")
wed = input("What were the total sales on Wednesday?")
thu = input("What were the total sales on Thursday?")
fri = input("What were the total sales on Friday?")
sat = input("What were the total sales on Saturday?")
summ = float(sun)+float(mon)+float(tue)+float(wed)+float(thu)+float(fri)+float(sat)
aver = format((float(sun)+float(mon)+float(tue)+float(wed)+float(thu)+float(fri)+float(sat))/7, '.2f')
print("Your total sales on Sunday were: $", sun)
print("Your total sales on Monday were: $", mon)
print("Your total sales on Tuesday were: $", tue)
print("Your total sales on Wednesday were: $", wed)
print("Your total sales on Thursday were: $", thu)
print("Your total sales on Friday were: $", fri)
print("Your total sales on Saturday were: $", sat)
print("Your total sales for the week was: $", summ)
print("Your average total sales per day was: $", aver)
