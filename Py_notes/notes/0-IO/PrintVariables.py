#variable is a storage container:x

x=4
x="bob"
x=3.14
x=["W",0,"rld"]
print(x)

#for eachItem in x:
#print(eachItem)
poop=6
toilet=7
iCouldAlsoUseThisAsAVariable=0
print(iCouldAlsoUseThisAsAVariable)


name = input("what is your name ")
print(name)

print("Hello there " + name)
school = input(name + ", What school do you go to outside of school outside of SICTC ")
subject = input("Ok, " + name + " at " + school + " what is your favorite subject? ")
 
#### MORE PROFESSIONAL METHOD OF PRINTING VAIRABLES###
#f-string fancy string == format strint

subject = input(f"Ok {name} at {school} what is your favoite subject")

grade = int(input(f" {name},What did you get on your last test?"))
print(f"Wow {name}, you got a {grade} in your {subject}   {x}")

'''
    Rules of thumb for variables 
    var = somthing and it can be almost anything
    print ="hello neighbor" But you overwrote the print function...

    1.cammleCase is most used in this course
    2.under_score_case is 2nd most used in this course
    3.either case, lowercase the first letter!!!!!!!!!!!!!!!!!!!!!!!!!!!
    4.don't be scared to reuse variables
    5.print often cuz your brain may not know what's there
'''
# CONSTANT Variables = a var that is always 1 value
GRAVITY = 9.81 
PI = 3.14
SCREEN_SIZE = 600
SPEED_OF_LIGHT = 300000000
print(GRAVITY)
GRAVITY = -9.81
print(GRAVITY)
