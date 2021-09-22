# Chapter 6 exercises
print("=" * 10, "Section 6.1 file input and output", "=" * 10)
file_variable = open("states.txt", "r")
file_variable.close()
state_capitals = open("capitals.txt", "w")
state_capitals.write("Alabama, Montgomery\n")
state_capitals.write("Alaska, Juneau\n")
state_capitals.write("Arizona, Phoenix\n")
state_capitals.close()
print("=" * 10, "Section 6.1 reading data from a file", "=" * 10)
states_data = open("states.txt", "r")
line1 = states_data.readline()
line2 = states_data.readline()
line3 = states_data.readline()
states_data.close()
print(line1, line2, line3)
print(line1)
print(line2)
print(line3)
print("=" * 10, "Section 6.2 use loops to process files", "=" * 10)
states_file = open("states.txt", "r")
counter = 0
for line in states_file:
    print(line)
    counter += 1
print("There were " + str(counter) + " lines.")
print("=" * 10, "Section 6.3 processing records", "=" * 10)
books = 3
books_file = open("books.txt", "w")
for book_info in range(1, books+1):
    title = input("What is the title of your favorite book?")
    auth = input("Who is the author of that book?")
    books_file.write(title + ", " + auth + "\n")
books_file.close()
print("=" * 10, "Section 6.4 exceptions", "=" * 10)
try:
    fail = open("superheros.txt", "r")
    fail.close()
except IOError:
    print("That file doesn't exist.")
