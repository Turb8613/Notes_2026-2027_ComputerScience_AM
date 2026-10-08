cardnumber = input("Please, input your credit card number: ")
print(f"***********{cardnumber[11:16]}")

website= input("What webste are you requesting: ")

if website.startswith("https"):
    print("secured")
else: print ("not secured")


