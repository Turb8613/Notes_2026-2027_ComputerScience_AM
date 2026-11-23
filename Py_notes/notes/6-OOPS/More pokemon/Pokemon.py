class Pokemon:
    def __init__(self,species,level,hp,moves):
                 self.species = species
                 self.level = level
                 self.hp = hp
                 self.moves = moves

    def getMoves(self):
        return self. moves


    def setSpecies(self):
        self.species = newSpecies


    def __str___(self):
                 novesormated = ", ".join(self.moves)
                 out=self.species+"\n"
                 out+=f"\t{self.level}\n"
                 out+=f"\t{self.hp}\n"
                 out+=f"\t{self.moves}"
                 return out

