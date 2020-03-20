j = int(input("How many digit is the number"))
number_array = []
for i in range(j):
    number= input("Number:")
    number_array.append(number)

if "." in number_array:
    print("That is a float")
else:
    print("That is a integer")
