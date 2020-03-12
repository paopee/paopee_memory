myheight=165
morestudent = "y"
countstudent = 0
tallest = 0
shortest = 188
smallestdifference = 0
tallestdifference= 0
yourheight = int (input("What is ur height?"))
while morestudent == "y":
    heightstudnet= int(input("What's the students height"))
    morestudent = input("more students? y/n")
    countstudent= countstudent+1
    if heightstudnet > tallest:
        tallest = heightstudnet
    if heightstudnet < shortest:
        shortest = heightstudnet
    smallestdifference = yourheight-shortest
    tallestdifference= yourheight - tallest

print ("your height subtract by the tallest in the class is %d"%(tallestdifference))
print (tallest)
print (shortest)




