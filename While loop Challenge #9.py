#Ex1 =
while True:
    subject = input ('What subject do u like?')
    if subject == "computerscience" :
        break
print ("Good")




subject = input ('What subject do u like?')
while subject != "computerscience":
    subject = input ('What subject do u like?')
    if subject == "computerscience":
        print ("Computerscience is the right ans")





#Ex2
number = 0

while number <15 or number >20:
    print ("Enter a number from 15 to 20")
    number = float(input("number:"))
