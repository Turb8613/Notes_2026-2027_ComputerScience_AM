'''
we can store items in theses items
first DB-
C - create
R - Read
U - Update
D - Delete data

list- 

array- WILL NOT BE USED

string- 

List Data Type
    Primitive Data Types
    Non - primitive data types
    
    Sequence data structures - iterable data
    List = one object with mutiple peices of data
    It's like a backpack or inventory

'''

#create
name=""
christmasList = []
groceryList = ["Turkey butts", "Ham","egg nog","sweet potato pie"]

genericlist= [1,"what",["O","l",2],name]
name="X"
print(genericlist)
christmasList.append("RTX5090")
christmasList.append("64 GB DDR5")
christmasList.append("NVIDIA Spark chip")

print(christmasList)

#read
print(christmasList)
print(christmasList[0])


christmasList.append("1 ham sandwich")
print(len(christmasList))
print(christmasList[-1]) #last item
print(christmasList[2:]) #item 2 to the end
#update

christmasList[1] ="32 GB DDR5"
print(christmasList)

newlist =groceryList + christmasList
print(newlist)

#delete

print("\n"*5)
print (newlist)
newlist[0]= ""
print(newlist)

item = newlist.pop()
print(item,newlist)

item = newlist.pop(3)
print(item,newlist)

del newlist[1]
newlist = []





####more usefull things###############


chessPiecesred=["pawn","rook","horse","cross","bishop","not cross"]
i=0
while(i<9):
    chessPiecesred.append("pawn")
    i+=1
print(chessPiecesred)

print(chessPiecesred.index("not cross"))
print(chessPiecesred)

if "not cross" in chessPiecesred:
    print("attack")
else:
    ("Long Live the queen")
print ("pawn" in chessPiecesred)
print (f"pawn count{chessPiecesred.count("pawn")}")
while(i!=8):
    chessPiecesred.pop(chessPiecesred.index("pawn"))
print(chessPiecesred)


