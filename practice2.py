height = float(input("please enter your height m: "))
weight = float(input("please enter your weight kg: "))

BMI = weight/(height*height)
print("your BMI is: ", BMI)

if BMI < 18.5:
    print("kamboode vazn!")
elif BMI >= 18.5 or BMI < 24.9:
    print("vazne ideal")
elif BMI >= 25 or BMI < 30:
    print("ezafe vazn!")
elif BMI >= 30 or BMI < 35:
    print("chaghi noe 1")
elif BMI >= 35 or BMI < 40:
    print("chaghi noe 2")
elif BMI >= 40:
    print("chaghi noe 3!")
