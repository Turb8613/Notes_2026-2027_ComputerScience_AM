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


q5 = input("Did primary bacup file generate?")
q6 ="6"
q7 ="7"

if q5 == "yes":
    q6 = input("Target destination nas or cloud?")
else: q7 = input("disk full or prossess timed out")

if q6 == "nas":
    print("Check local SMB storage quota")
else: print("Check AWS s3 bucket write permissions")

if q7 == "full":
    print("trigger disk cleanup aleart")
else: print("restart backup service daemon")

q8 = input("Enter role: student or visitor").lower()
q9 ="9"
q10 ="10"
q11 ="11"
q12 ="12"
q13 ="13"
q14 ="14"
q15 ="15"
q16 ="16"

if q8 == "visitor":
    q9 = input("do they have a pre-sceduled appointment")
else: q10 = input("do they have a student badge with them")

if q10 == "yes":
    q11 = input("is their lab waver signed")
else:
    print("report to the office for a temporary badge ")
if q11 == "yes":
    print ("access granted the door to the lab is unlocked")
else:
    print("Must complete digital lab safty quiz before entry")

if q9 == "yes":
    q12 = input("is staff present at the door")
else: print("go to the receptionist and wait for somone to assist you")

if q12 =="yes":
    print("issue guest pass")
else: print("must wait for escort")


q13= input("do you hear a creeper hissing")

if q13 == "yes":
    q14 = input("is there a water bucket in your hotbar")
else: 
    q15 = input("is your hunger bar empty")

if q14 == "yes":
    print("MLg clutch it with the bucket")
else: q16 = input("Did you dig streght down")

if q16 == "yes": print("Fell into lava diamonds gone player tried to swim in lava")
else: print("shield up! Blown 20 blocks back into the wall of a ravine")

if q15 == "yes": q17 = input("eat rotten flesh")
else: print("build a 3x1 piller and cry untill dawn")

if q17 == ("yes"): print("hunger effect active but you baerly survived!")
else:print("starved to death wile looking at a cow respawn screen")

q18 = input("Is the hallway bathroom closed for cleaning?")
if q18 == "yes":
    q18 = input("Can you clean & hold for 15 min?")
    if q18 == "yes":
        print("waddles")
    elif q18=="no":
        q18=input("Risk the creepy locker room?")
        if q18 == "yes":
            print("creepy restroom")
        elif q18 == "no":
            print("nurse visit")
elif q18 == "no"
    q18 = input("is there toilet paper?")
    if q18 == "yes":
        q18 = input("does the door lock?")
        if q18 == "yes":
            print("relief")
        elif q18 == "no":
            print("hold with your feet")
    elif q18 == "no":
        q18 = input("towles or hall pass?")
        if q18 == "yes":
            print("averted")
        elif q18 == "no":
            print("call your friend")
else:
    print("what?")
