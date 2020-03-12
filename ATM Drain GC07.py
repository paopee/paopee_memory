Pooja_bank = 1000

ans = input("Do you want to withdrawl money? y/n")
while ans == "y":
    withdraw = float (input("Amount Withdrawl:$"))
    while withdraw %5 != 0:
        print("error")
        withdraw = float (input("Amount Withdrawl:$"))

    Pooja_bank = Pooja_bank - withdraw -0.5
    if Pooja_bank <0 :
        print("Exceeds limits")
        print("Your account:", Pooja_bank)
    else:
        print("Success")
        print("Remaining total in account:",Pooja_bank)

    ans = input("Do you want to withdrawl money? y/n")
    if ans == "n":
        print("Restart code")

else:
    print("Restart code")
