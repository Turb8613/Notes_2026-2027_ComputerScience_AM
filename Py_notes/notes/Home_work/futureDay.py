answer=0
day=0
today=int(input("Enter todays day mon=1 saturday=6 "))
if today==1: print("today is monday")
elif today==2: print ("today is tuesday")
elif today==3: print ("today is wendsday")
elif today==4: print ("today is thursday")
elif today==5: print ("today is friday")
elif today==6: print ("today is saturday")
else: print ("today is sunday")

pased=int(input("How manny days passes"))
day= pased + today

if day > 7:
    answer = day-7

if answer==1: print("today is monday")
elif answer==2: print ("today is tuesday")
elif answer==3: print ("today is wendsday")
elif answer==4: print ("today is thursday")
elif answer==5: print ("today is friday")
elif answer==6: print ("today is saturday")
else: print ("today is sunday")