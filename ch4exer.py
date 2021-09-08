# Chapter 4 Exercises
print("=" * 10, "Section 4.2 condition controlled loop", "=" * 10)
num = 10
while num >= 0:
    print(num)
    num = num - 1
print("")
print("=" * 10, "Section 4.3 for loop", "=" * 10)
for day in ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"):
    print(day)
print()
print("=" * 10, "Section 4.3 using range() in a for loop", "=" * 10)
for rnum in range(1, 11):
    print(rnum)
print()
print("=" * 10, "Section 4.4 running total", "=" * 10)
total = 0
dig = 0
nums = int(input("How many scores?"))
for score in range(1, nums+1):
    dig = int(input("enter test score:"))
    total += dig
print(total)
print()
print("=" * 10, "Section 4.5 sentinel value", "=" * 10)
count = 0
done = 1
total = 0
print("Enter 0 when you are done.")
while done and not 0:
    score = int(input("Enter test score:"))
    if score == 0:
        done = 0
    count += 1
    total += score
print(total)
print("=" * 10, "Section 4.6 data validation loop", "=" * 10)
done = 1
while done and not 0:
    score = int(input("Enter a number between 1 and 10:"))
    if score > 10:
        done = 1
    elif score < 1:
        done = 1
    else:
        done = 0
    if done == 1:
        print(score, "is an invalid entry")
    else:
        print(score, "is a valid entry")
