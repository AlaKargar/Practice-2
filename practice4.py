import random
z=True
while z!=False:
  x = (random.randint(1,6))
  print(x)
  if x == 6:
    print("again!")
    y= (random.randint(1,6))
    print(y)
    z=False
    break
