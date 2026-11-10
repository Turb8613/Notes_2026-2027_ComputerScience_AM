'''
    functions are abstraction
    define function(what is needed to run it):
        do this algorithm

    then you call your function
    add(x,y)
    f(x)
    fun()
'''

x = 4
y = 4
def add(x,y):
    print(x+y)

add(x,y)    #positional arguments
add(4,4)    #first arg is x and the next is y
add  (2,2)  #apparently this is ok...
add("2","2")
add([1,2],[3,4])

def sub(x,y):       #local variables
    print(x-y)

def subtract(x,y):
    print(x-y)

def minus(a,b):
    print(a-b)

#this multiplies the two input variables
def mandm(red,green):  #name your f(x) appropriately
    print(red*green)

mandm(2,8)
mandm("6",7)

'''
    RULE OF THUMBS
    1. name things appropriately - f() are verbs
    2. comments will save you later in life
    3. get rid of the complexity KISS
    4. don't start with the f(x), build the algo then refine it to a function
        as in look for repeating code
        you want D.R.Y code
        Dont
        Repeat
        Yourself
'''

#check for user input - want the program to stop until correct input
def checkInput(question,answers):
    response=input(question)
    while(not(response in answers)):
        response=input(question)

def checkNumberInput(question,answers):
    response=int(input(question))
    while(not(response in answers)):
        response=input(question)


checkInput("Would you like an apple pie with that? ",["yes","no","y","n","yeah","yay","nay","nah"])

name = input("what is your name? ")
#age = input("what is your age? ")
age = checkNumberInput("What is your age? ",range(13,230))





