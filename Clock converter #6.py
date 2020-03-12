time = float(input("What time is it now"))
amorpm= input("is it am or pm")


if amorpm == "am":
    print ("it is already in 24 hours")
else:
    time= time + 12
    print ("this is in 24 hours %3f " %(time))
