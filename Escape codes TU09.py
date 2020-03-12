count = 0
import random
while True:
    MyNumber = random.randint(1,2000000)
    try:
        valid_number = int(MyNumber)
        break
    except ValueError:
        print("Seriously, don't you read the instructions. \nI asked for a number...")
        count = count +1

print(valid_number)
print (count, "errors")
