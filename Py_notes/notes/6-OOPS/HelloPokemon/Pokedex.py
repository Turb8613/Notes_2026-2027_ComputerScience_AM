#import
from Pokemon import Pokemon

#global var
#object = Constructor()
myPokedex= []
myPokedex.append(Pokemon("Bulbasaur","bub",5,"Grass",16))
myPokedex.append(Pokemon("Ivysaur","Ivy",25,"Grass",56))
myPokedex.append(Pokemon("Venasaur","Venus fly trap",50,"Grass",160))
myPokedex.append(Pokemon("Charmander","Burny",5,"Fire",16))




for i in range(len(myPokedex)):
    print(f"{i+1}{Pokemon}")
