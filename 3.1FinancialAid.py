# Financial Aid Questions:
cs = input("Are you a new student or returning student? (enter n or r)")
GPA = int(input("What is your current GPA?"))
crimrec = input("Do you have a criminal record in drugs? (enter y or n)")
cred = int(input("How many credit hours are you currently enrolled in?"))
gyi = int(input("What is your gross yearly income?"))
if GPA >= 2 and crimrec == "n" and cred >= 6 and gyi < 50000:
    print("You are eligible to apply for financial aid.")
else:
    print("You are not eligible for financial aid.")
