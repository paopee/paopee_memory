number_list = []


import random
for i in range(50):
    number = random.randint(0,10)
    number_list.append (number)

print("List:", number_list)
print("Minimum:",min(number_list))
print("Maximum:", max(number_list))
print ("Mean average:", (sum(number_list)/len(number_list)))
