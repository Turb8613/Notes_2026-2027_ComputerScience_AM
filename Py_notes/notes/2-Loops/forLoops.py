''' 
for var in list:
for each item in my list: 
for i in list:
for i in range:

    That list will set up how many iterations you have

'''

for eachItem in [0,1,2,3,4,5,6,8,9]:
    print(eachItem,end=",")

print()
#range makes a lists of numbers
#range(start value,end value,step)
for eachItem in range(100):
    print(eachItem,end=",")

for i in range(0,21,2):
    print(i)
for i in range(0,21,3):
    print(i)
for i in range(0,101,20):
    print(i)
for i in range(1,10,-1):
    print(i)
'''   
for i in range(65,91):
    print(chr(i)
'''
classroom=['bill','bo','baggins','brett','brayden']
subject=["math",'physics','lunch','cs','government']

for i in range(5):
    print(f"{classroom[i]}'s favorite class is {subject[i]}")


for i in range(len(classroom)):
    print(f"{classroom[i]}'s favorite class is {subject[i]}")

first=["jim","jhon","jo","jon","james","jared","jarrot","j"]
last=["bo","smith","robert","snow","cameron","diamon","orleans","k"]

print()
for i in range(len(first)):
    print(f"{first[i]}.{last[i]}@evsck12.com")


word,letter = "mississippi","i"
count=0
for eachLetter in word:
    if eachLetter == letter:
        count+=1
print(count)


count=0
word ="McDonald's Play Place"
letter = ["a","e","i","o","u"]
for eachLetter in word:
    if eachLetter == letter:
        print(f"{eachLetter}")
