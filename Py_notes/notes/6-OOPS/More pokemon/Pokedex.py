from Pokemon import Pokemon

pokedex = []

#read in the data from the date
#         filename  read only
with open("Gen1.txt","r") as file:
    # r is for read only
    lines = file.readlines()

#save the data to a pokedex list
for eachLine in lines[1:]:
    parts = eachLine.rstrip().split(",")
#    print(parts[5:])

    pokedex.append(Pokemon(parts[0],parts[3],parts[4],parts[5:]))
#functions

#mainLoop

#print out eachItem in poekList
print(f"Total Pokemon Imported: {len(pokedex)}")

#for eachPokemon in pokedex:
#   print(eachPokemon)

'''
    ask user for a pokemon, if they ask for one in the db
    output:
        level species has the following attacks
            attack 1
            attack 2
            attack 3

        no need to loop the program untill they say quit
        just one time is nessary
'''

pdb = input("what pokemon are you looking for ")
if pdb in pokedex:
    print("true")

else: print("false")

