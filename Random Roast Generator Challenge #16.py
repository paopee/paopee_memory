roast = ["Shut up", "Big L for", "U suck"]

import random
ans = "y"

roasted = random.choice(roast)
name = input("who do u want to roast name:")
print (roasted, name)

while ans == "y":
    roasts = input("Input a insult")
    roast.append (roasts)
    print(roast [3])
    ans = input("Do u want to input another one y/n?")

print (roast)
