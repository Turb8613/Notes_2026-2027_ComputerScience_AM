import math
import cmath

problem1 =((8/2)+4*16)/3*8
problem2 =(2/81)/(3/7)*8*(2+1*12)
problem3 =(4-2)**2+(16-2)**2
problem4 =math.sqrt((7-1/2)**2+(1/3-4)**2)

print(f"1. {problem1}")
print(f"2. {problem2}")
print(f"3. {problem3}")
print(f"4. {problem4}")

print(8^2) #bitwise calcualtion... IDK

#return a whole number when I devide

print (math.floor(7/3))
print(7//3) #int devide
#Trunkates the decimal as in cuts the desimal off

#find the remainder? ... modulus

print(7%3)
print(8%2)

a=2
b=4
c=-7


#you will have to do it twice....

xb=b-math.sqrt(b**2-4*a*c)/(2*a)
xp=b+math.sqrt(b**2-4*a*c)/(2*a)

print(f"The Roots are: {xp:.2f} and {xb:.2f}")

print(cmath.sqrt(-4))
print(1j*2j)
print(complex(2,3))

#imput funct brings
subtotal = eval(input("What is the subtotal: "))
#eval makes py figure it out
#int() converts it to a int
#float() converts to a float
#str() string 
#bool() true or false boolean
tax = subtotal *0.7
total = subtotal + tax
print(subtotal,tax,total)

subtotal*=1.07 # same as subtotal=subtotal*0.7
'''
Math operator
+,-,*,/
+= -= *= /=
=

not,!,!=,==,<,>,<=,>=
'''

