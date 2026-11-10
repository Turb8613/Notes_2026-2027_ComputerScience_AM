#import
from distaceConversion import * #*=everything
#from file import f(x)


#global variables/objects
menu = '''
    in to ft (if)           mph to kph (mk)
    ft to in (fi)           kph to mph (km)

    tbsp to tsp (tbts)      lbs to kg (lk)
    tsp to tbsp (tstb)      kg to lbs (kl)

    c to f (cf)             oz to cups (oc)
    f to c (fc)             cups to oz (co)

    stop (stop)

What would you like to do?
'''

#f(x)

#main loop
user = input(menu)
while(user!="stop"):
    #algo
    if user =="if":
        print(in2ft(float(input("inches: "))))
    elif user =="cf":
        print(c2f(float(input("celcius: "))))
    elif user =="fc":
        print(f2c(float(input("ferenhight: "))))
    elif user == "fi":
        pass                #pass to the next itteration
    elif user == "mk":
        pass                #great placeholder
    elif user == "km":
        pass
    else:
        print("I'm sorry I didn;t quite get that")

    user=input(menu)

