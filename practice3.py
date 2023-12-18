name= input("please enter your name and last name: ")
unit1= float(input("please enter your English mark: "))
unit2= float(input("please enter your Persian mark: "))
unit3= float(input("please enter your Math mark: "))

avg= (unit1+unit2+unit3)/3
print("your avg: ", avg, name)
if avg <=10:
    print("Fail")
elif avg > 10 and avg < 18:
    print("good")
elif avg >= 18:
    print("perfect!")
else:
    print("invalid number!")