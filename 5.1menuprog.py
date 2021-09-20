# Menu programming code:
print("Select one of the food items below to learn more\n1. Angel Food Cake\n2. Pancakes\n3. Zucchini Bread\n4. French Toast\n5. Banana Bread")
h = input("Enter the number of your choice:")


def one():
    print("Angel Food Cake is a very soft, fluffy, and sweet cake.")
    print("They are very low in calories compared to other cakes.")


def two():
    print("Pancakes are soft and round batter cooked to a perfect browned color.")
    print("They are best served with syrup.")


def three():
    print("Zucchini bread is a slice of a loaf of bread made with several")
    print("ingredients with the main being Zucchini.")


def four():
    print("French toast is a batch of bread soaked with a mixture of eggs and seasonings.")
    print("It is then cooked on a pan to perfection.")


def five():
    print("Banana bread is a slice of a loaf of bread made with several")
    print("ingredients with the main being Bananas.")


if h == '1':
    one()
elif h == '2':
    two()
elif h == '3':
    three()
elif h == '4':
    four()
elif h == '5':
    five()



