pay = 0
print("Number 1:Coke\nNumber 2:Sprite\nNumber 3:Pepsi")

while True:
    enter = int(input("Enter item number:"))
    if enter == 1 or enter == 2 or enter == 3:
        break

if enter ==1 :
    pay = 3
    print("$3.00")


if enter ==2 :
    pay = 2
    print("$2.00")

if enter == 3:
    pay = 4
    print("$4.00")

cash_in = float(input("Enter amount: "))
while cash_in < pay:
    print("Underpayment")
    cash_in = float(input("Enter amount: "))

if cash_in == pay:
    print("Payment success")
else:
    print("Payment success")
    change = cash_in - pay
    print("Here is your change:", change)



