ui = input("Hey, guess what? ")
while(ui!="Wsp"):
    ui = input("Hey, guess what? ")
print("Turky Butt")
print()


''' 
ask the user for a number between 1 and 10 
if the user guesses wrong tell them to guess again
and if they get it print congrats
'''


sn = 1
numb=input("guess a number")
numb=int(numb)
while numb != sn:
    if numb == sn:
        print("you got it")

    else:
        if numb > sn :
            print("guess lower")
        else: print("Guess higher")


