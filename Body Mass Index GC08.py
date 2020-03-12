weight = float(int(input("Weight:")))
height = float(int(input("Height:")))

BMI = weight / height **2

if BMI<18.5:
    print ("Underweight")
elif 18.5<=BMI<25.0:
    print ("Normalweight")

elif 25.0<=BMI<30.0:
    print("Over weight")

elif BMI>=30:
    print("Obesity")



