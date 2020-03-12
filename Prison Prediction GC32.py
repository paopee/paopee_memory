import random
user = input ("You are a prisoner, do you want to confess or stay silent")
computer = random.choice(["confess","stay silent"])

print (computer)



if user == "stay silent" and computer == "confess":
    print ("You go to jail for 20 years")
    print ("The other prisoner is relesed")

elif user == "stay silent" and computer =="stay silent":
    print ("Both of you are in prison for only one year ")

elif user == "confess" and computer == "confess":
    print ("Both of you are in jail for 5 years")


