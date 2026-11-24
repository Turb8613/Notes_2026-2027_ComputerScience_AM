quarters = 0
dimes = 0
nickles = 0
pennies = 0

change_cents = round(float(input("How much change do you need back? ")) * 100)

while change_cents >= 25:
    change_cents -= 25
    quarters += 1

while change_cents >= 10:
    change_cents -= 10
    dimes += 1

while change_cents >= 5:
    change_cents -= 5
    nickles += 1

while change_cents >= 1:
    change_cents -= 1
    pennies += 1

print(f"""
Quarters: {quarters}
Dimes: {dimes}
Nickels: {nickles}
Pennies: {pennies}
""")