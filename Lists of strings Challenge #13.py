MyList = ["Kuala Lumpur","London","Paris","New York","Bangkok"]
MyList.append ("Beijing")
MyList.remove("Kuala Lumpur")
Newcity = input("Input a city")
MyList.append(Newcity)
MyList.sort()
print (MyList)

List = ["Lemow","Lol","Hey","Wassu"]
print(List [0:4])

list = []
count = 0
while count <4:
    Characters = input ("Input game characters")
    count = count+1
    list.append (Characters)

list.sort()
print (list)
