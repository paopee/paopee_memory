import random

#random integer
mynumber = random.randint(0,100)

print (mynumber)

#random float
mynumber = random.uniform(0.1,9.9)

print (round(mynumber,2))


import random
Coin_Toss = random.choice(["Heads","Tails"])
print(Coin_Toss)

import random
lists = ["James","Kevan","Dickson","Jacky","Mike"]
for i in range (5):
    name = random.choice(lists)
    print (name)
    keep = input("do you wish to keep the name in the list y/n")
    if keep == "y":
        print ("ok next")
    else:
        lists.remove(name)


print (lists)



