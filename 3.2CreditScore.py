# credit rating finder:
cred = int(input("What is your credit score?"))
if cred >= 720:
    print("Your credit score of ", cred, " Is excellent.")
elif cred >= 690:
    print("Your credit score of ", cred, " Is good.")
elif cred >= 630:
    print("Your credit score of ", cred, " Is fair.")
elif cred >= 300:
    print("Your credit score of ", cred, " Is bad.")
