'''
boolean data type == T or F == True or False

    conditionals = Code that does somthing
        Usually the condition is a boolean 

        if booleanExpression == True:
            then do this
        elif booleanExpression == True:
            then do this
        else:
            then do this 
'''

x = True
y = False

print(x,y)

print(10 > 5)

'''
    Logic Operators
        < > <= >=
        == if its equal to 
        = sets things equal to 
        is -> checks if the memory location is the same
        not or ! => opposite of the boolean to the right 

'''

if x == y:
    print("you may proceed")
#if x and y are not the same it does nothing 

if x == (not y):
    print("you may not proceed")

x,y = 0,0
y= 2*+4

print(0 == y)
y < 2* x +4
if( 0<y):
    print("shade twords 0")
else:
    print("shade away from 0")
    # If all else fails do this statement 

if( 0<y):
    print("shade twords 0")
elif (y == 0):
    print("y dose equal 0")
else:
    ("shade away from zero")

temp = int(input("What is the temperature of the water? "))
if temp <= 32:
    print("SOLID")
if temp >= 212:
    print("GAS")
else:
    print("Liquid")

'''
    Rules of thumbs:
        1. Figure out how many outputs there will be 
            1.a: If 3 outputs then if elif else 
            Example -> if 4 outputs then if, elif, elif, else
            if 2 -> if, else 
            BUT you dont alway need an else 

        2. If nothing needs to happen if all else fails 
            then don't have the else 
'''

'''
    Compound conditionals or Complex conditionals
        and -> boolean == True and boolean==True
            bolth sides of the and are true
                then the result is true
        or -> only one side nees to be true
'''

username = "eli"
password = "123456"

if username == "eli" and password == "123456":
    print(f"Welcome {username}")


'''
    Weird things of python
        if int or str is either 0 or blank
        it is false
        else:
        anything other than 0 or blank or true
'''


