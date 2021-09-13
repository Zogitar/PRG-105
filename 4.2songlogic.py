# Song Logic Coding:
bottle = 99
stop = 1
while stop and not 0:
    print(bottle, "bottles of beer on the wall,\n", bottle, "bottles of beer\n", "Take one down, pass it around")
    bottle -= 1
    print(bottle, "bottles of beer on the wall\n")
    if bottle == 2:
        stop = 0
print(bottle, "bottles of beer on the wall,\n", bottle, "bottles of beer\n", "Take one down, pass it around\n", "1 bottle of beer on the wall\n")
print("1 bottle of beer on the wall,\n", "1 bottles of beer\n", "Take one down, pass it around\n", "0 bottle of beer on the wall\n")
