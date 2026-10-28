import math
x1=input("what is the first X")
y1=input("what is the first Y")
x2=input("what is the second X")
y2=input("what is the second Y")

y1= int(y1)
y2= int(y2)
x2= int(x2)
x1= int(x1)

xa= x2-x1
ya= y2-y1
ya=ya*ya
xa=xa*xa
a=ya+xa
a=a ** 0.5

print(f"The distance is {a}") 