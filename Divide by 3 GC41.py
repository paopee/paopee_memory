number = float(input("Number:"))

sum = number%3
if sum == 0:
    print("Your number is divisible by 3")
else:
    print("Your number is not divisible by 3")
    print("Remainder",sum)
