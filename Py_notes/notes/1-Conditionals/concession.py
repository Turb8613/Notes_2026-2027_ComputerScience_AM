#iteration 1 -popcorn
'''
ask the user what size popcorn they want
    small - $5.00
    medium - $6.00
    large -$7.00
    print out their total
        subtotal: $_._
'''
small = 5.00
medium = 6.00
large = 7.00
popcorn = ("test")
q2 = ("test2")
subtotal=0
popcorn = input("do you want popcorn")
if popcorn == ("yes"):
    q2=input("what size popcorn do you like S,M,L").lower()
else:q2="n"
print("thank you enjoy your movie")

if q2 == ("s"):
    subtotal+=5
elif q2 == ("m"):
    subtotal+=6
elif q2 == ("l"):
    subtotal+=7

print(f"subtotal: ${subtotal}")

#iteration 2 -pop
soda = input("do you want a soda today y/n").lower()
so = "Plan"
if soda == ("y"):
    so =input('''
        "what size aod do you like
        (S) Small =$3.00
        (M) Medium =$4.00
        (L) Large =$5.00
''').lower()
else: so="n"
if so =="s":
        subtotal+=3
elif so =="m":
        subtotal+=4
elif so =="l":
    subtotal+=5
    input("would you like to upgrade to a child size for an extra $0.38 today")=="y"
    subtotal+=.38 

print(f"subtotal: ${subtotal}")
#iteration 3 -candy
candy=("none")
candytype = ("yum")
'''
    Do you want any candy?
        What type of candy do you want
        mnm
            plain
            peanut
            pb
            mini
        skittles
            regular
            tropical
        worlds finest chocolate bars -2
            wafer
            milk chocolate
            dark chocolate
            almonds
            caramel
        recce's-2
        nerds gummy clusters
'''
candyquestion =input("do you want a candy")
if candyquestion == ("yes"):
    candytype =input('''
The candys we have are
M&M's (M)- $2.50
Skittles (S)- $2.50
Worlds fines chocolate (W)- $2
Reece's (R)- $2
Nerds gummi clusters (G)- $3
What would you like?
                     ''').lower()
else:candytype ="n"
if candytype == "s":
    candyflavor = input('''
What flavor do you want
    (s1)regular
    (s2)tropical
    ''')
    subtotal+=2.50

elif candytype == "m":
    
    candyflavor = input('''
What flavor do you want
    (m1)plain
    (m2)peanut
    (m3)pb
    (m4)mini
    ''')
    subtotal+=2.50

elif candytype == "w":
    
    candyflavor = input('''
What flavor do you want
    (w1)wafer
    (w2)milk chocolate
    (w3)dark chocolate
    (w4)caramel
    ''')
    subtotal+=2

elif candytype == "r":
    subtotal+=2

elif candytype == "g":
    subtotal+=3

print(f"subtotal: ${subtotal}")
#iteration 4 -butter
pump= input("how many pumps do you want")
subtotal += int(pump)*0.25 
print(f"subtotal: ${subtotal}")

#iteration 5 -print
discount="Na"
if not(q2 == "n"or so == "n" or candytype == "n"):
    print("Here is a discount for a dollar off")
    subtotal -= 1
    discount=True

print(f'''

    Your order:
        popcorn = {q2}
        drink = {so}
        candy = {candytype}
        butter ={pump}

        discount ={discount}

        subtotal ={subtotal}
        tax = {subtotal * .07}
        total ={subtotal * 1.07}
'''
      )
