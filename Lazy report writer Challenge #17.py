comments = ["Try to improve in grammar","Improve on your spelling","Revise more before the test","Check your ans"]

numberofstudents = int(input ("How many students are there in your class"))
count = 0

while count < numberofstudents:
    import random
    ans = random.choice(comments)
    print ("teacher's comment:",count,ans)
    count = count +1
