# TODO 9.1 Dictionaries
import pickle
print("=" * 10, "Section 9.1 dictionaries", "=" * 10)
# 1) Finish creating the following dictionary by adding three more people and birthdays
birthdays = {'Meri': 'May 16', 'Kathy': 'July 14'}
birthdays["Amber"] = "August 10"
birthdays["Klee"] = "July 27"
birthdays["Yoimiya"] = "June 21"

# 2) Print Meri's Birthday
print(birthdays['Meri'])

# 3) Create an empty dictionary named registration
registration = {}

# You will use the following dictionary for many of the remaining exercises"
miles_ridden = {'June 1': 25, 'June 2': 20, 'June 3': 38, 'June 4': 12, 'June 5': 30, 'June 7': 25}

# 1) Print the keys and the values of miles_ridden using a for loop
for eggs in miles_ridden:
    print(eggs + ", " + str(miles_ridden[eggs]))

# 2) Get the value for June 3 and print it, if not found display 'Entry not found', replace the ""
if "June 3" in miles_ridden:
    value1 = miles_ridden['June 3']
else:
    value1 = "Entry Not Found"
print(value1)

# 3) Get the value for June 6 and print it, if not found display 'Entry not found' replace the ""
if "June 6" in miles_ridden:
    value2 = miles_ridden['June 6']
else:
    value2 = "Entry Not Found"
print(value2)

# 4) Use the values method to print the miles_ridden dictionary
print(miles_ridden.values())

# 5) Use the keys method to print all of the keys in miles_ridden
print(miles_ridden.keys())

# 6) Use the pop method to remove June 4 then print the contents of the dictionary
miles_ridden.pop("June 4")
print(miles_ridden)

# 7) Use the items method to print the contents of the miles_ridden dictionary
print(miles_ridden.items())

# TODO 9.2 Sets
print("=" * 10, "Section 9.2 sets", "=" * 10)
# 1) Create an empty set named my_set
my_set = set()

# 2) Create a set named days that contains the days of the week
days = set(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])

# 3) Get the number of elements from the days set and print it
print(len(days))

# 4) Remove Saturday and Sunday from the days set
days.remove("Saturday")
days.remove("Sunday")

# 5) Determine if 'Mon' is in the days set
if "Mon" in days:
    print("Mon is in days")
else:
    print("Mon is not in days")

# TODO 9.3 Serializing Objects (Pickling)
print("=" * 10, "Section 9.3 serializing objects using the pickle library", "=" * 10)
# 1) Import the pickle library at the top of this file

# 2) Create the output file log and open it for binary writing
output = open("file_log.dat", "wb")

# 3) Pickle the miles_ridden dictionary and output it to the log file
pickle.dump(miles_ridden, output)

# 4) Close the log file
output.close()
