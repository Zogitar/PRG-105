# 10.2 Trivia Game Coding:

# 10.1 Class Coding used as outline:

class P:
    def __init__(self, player, question, a1, a2, a3, a4, answer):
        self.__player = player
        self.__question = question
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__answer = answer

    def set_player(self, player):
        self.__player = player

    def set_question(self, question):
        self.__question = question

    def set_a1(self, a1):
        self.__a1 = a1

    def set_a2(self, a2):
        self.__a2 = a2

    def set_a3(self, a3):
        self.__a3 = a3

    def set_a4(self, a4):
        self.__a4 = a4

    def set_answer(self, answer):
        self.__answer = answer

    def get_player(self):
        return self.__player

    def get_question(self):
        return self.__question

    def get_a1(self):
        return self.__a1

    def get_a2(self):
        return self.__a2

    def get_a3(self):
        return self.__a3

    def get_a4(self):
        return self.__a4

    def get_answer(self):
        return self.__answer

    def __str__(self):
        return "This question is for " + self.__player + "\n" + self.__question + "\n" + self.__a1 + "\n" + self.__a2 + "\n" + self.__a3 + "\n" + self.__a4 + "\n" + self.__answer


def questions():
    q1 = P("Player 1", "How many dragon balls are on earth?", "A. 5", "B. 7", "C. 14", "D. 11", "Input the letter you choose:")
    q2 = P("Player 2", "What jutsu did Naruto steal?", "A. Sharingan", "B. Summoning Jutsu", "C. Shadow Clone Justu", "D. Rasengan Jutsu", "Input the letter you choose:")
    q3 = P("Player 1", "What layer of the abyss did Riko enter at the end of the latest movie?", "A. 3", "B. 4", "C. 5", "D. 6", "Input the letter you choose:")
    q4 = P("Player 2", "What is the name of Reiner Braun's titan?", "A. Armoured Titan", "B. Attack Titan", "C. Warhammer Titan", "D. Colossal Titan", "Input the letter you choose:")
    q5 = P("Player 1", "Who is ash's first pokemon?", "A. Charmander", "B. Pikachu", "C. Squirtle", "D. Bulbasaur", "Input the letter you choose:")
    q6 = P("Player 2", "What sport is played in Haikyuu?", "A. Volleyball", "B. Basketball", "C. Golf", "D. Paint Ball", "Input the letter you choose:")
    q7 = P("Player 1", "What sport is played in Kakegurui?", "A. Dodge Ball", "B. Swimming", "C. Softball", "D. Gambling", "Input the letter you choose:")
    q8 = P("Player 2", "What instrument does the male protagonist of Your Lie in April play?", "A. Keyboard", "B. Guitar", "C. Violin", "D. Piano", "Input the letter you choose:")
    q9 = P("Player 1", "What country do the K-On! girls visit?", "A. France", "B. Canada", "C. United States", "D. Europe", "Input the letter you choose:")
    q10 = P("Player 2", "What eye does Lelouch have his Geass in?", "A. Left", "B. Right", "C. Both", "D. Neither", "Input the letter you choose:")

    p1 = 0
    p2 = 0
    fir = input(q1)
    for ans in fir:
        if ans == "b":
            print("That answer is correct")
            p1 += 1
        elif ans == "B":
            print("That answer is correct")
            p1 += 1
        else:
            print("That is incorrect\nThe correct answer is B")
        print("\n")

    sec = input(q2)
    for ans in sec:
        if ans == "c":
            print("That answer is correct")
            p2 += 1
        elif ans == "C":
            print("That answer is correct")
            p2 += 1
        else:
            print("That is incorrect\nThe correct answer is C")
        print("\n")

    thi = input(q3)
    for ans in thi:
        if ans == "d":
            print("That answer is correct")
            p1 += 1
        elif ans == "D":
            print("That answer is correct")
            p1 += 1
        else:
            print("That is incorrect\nThe correct answer is D")
        print("\n")

    fou = input(q4)
    for ans in fou:
        if ans == "a":
            print("That answer is correct")
            p2 += 1
        elif ans == "A":
            print("That answer is correct")
            p2 += 1
        else:
            print("That is incorrect\nThe correct answer is A")
        print("\n")

    fiv = input(q5)
    for ans in fiv:
        if ans == "b":
            print("That answer is correct")
            p1 += 1
        elif ans == "B":
            print("That answer is correct")
            p1 += 1
        else:
            print("That is incorrect\nThe correct answer is B")
        print("\n")

    six = input(q6)
    for ans in six:
        if ans == "a":
            print("That answer is correct")
            p2 += 1
        elif ans == "A":
            print("That answer is correct")
            p2 += 1
        else:
            print("That is incorrect\nThe correct answer is A")
        print("\n")

    sev = input(q7)
    for ans in sev:
        if ans == "d":
            print("That answer is correct")
            p1 += 1
        elif ans == "D":
            print("That answer is correct")
            p1 += 1
        else:
            print("That is incorrect\nThe correct answer is D")
        print("\n")

    eig = input(q8)
    for ans in eig:
        if ans == "d":
            print("That answer is correct")
            p2 += 1
        elif ans == "D":
            print("That answer is correct")
            p2 += 1
        else:
            print("That is incorrect\nThe correct answer is D")
        print("\n")

    nin = input(q9)
    for ans in nin:
        if ans == "d":
            print("That answer is correct")
            p1 += 1
        elif ans == "D":
            print("That answer is correct")
            p1 += 1
        else:
            print("That is incorrect\nThe correct answer is D")
        print("\n")

    ten = input(q10)
    for ans in ten:
        if ans == "a":
            print("That answer is correct")
            p2 += 1
        elif ans == "A":
            print("That answer is correct")
            p2 += 1
        else:
            print("That is incorrect\nThe correct answer is A")
        print("\n")

    if p1 > p2:
        print("Player one wins!!")
    elif p2 > p1:
        print("Player two wins!!")
    elif p1 == p2:
        print("The results are a draw!")

    print("Player one scored", p1, "out of 5 points!!")
    print("Player two score", p2, "out of 5 points!!")


questions()
