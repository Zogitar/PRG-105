# 8.1 Acronym Coding
name = input("Input a phrase you would like to turn into an acronym: ")
namsp = name.split()
acr = ""
for word in namsp:
    acr += word[0]
acr = acr.upper()
print(acr)
