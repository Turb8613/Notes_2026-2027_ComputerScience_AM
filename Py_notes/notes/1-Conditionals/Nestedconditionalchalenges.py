q1 = input("did you restart the computer ")
q2 ="2"
q3 ="3"
q4 ="4"

if q1 == "yes":
    q2 = input("Did you restart thw PC or just the monitor? ")        
else: q3 = input("Is the power strip plugged into it's self ")

if q2 == "pc":
    q4 = input("Is the ethernet cable plugged in to the wall ")
else: print("please turn of the box on the ground ")

if q3== "yes":
    print("please unplug it from it's self and plug it into the wall")
else: print("restart it right now. Ticket closed.")

if q4 == "yes":
    print("Its a DNS issue its always dns. ESCALATE TO TIER 3")
else: print("plug it in Wifi does not come from the air.")
