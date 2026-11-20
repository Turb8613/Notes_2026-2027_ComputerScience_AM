'''
    classes and objects
    primitive = bool, int, float, character
    non primitive = string, list, json
        classes and objects => YOUR OWN DATA TYPE

    rules of thumbs
    1. Do you need a var that stores a lot of things and does a lot of stuff?
    2. Do you need soeme type of abstract consept that is reusable
    3. Do you need to stop repetive code
    4.Your classes should be in a seprate file
    5.Your files name should be the same as your class*
    6. Capatilization is key to state if you're using a class or an object
    8.COMMIT YOUR CODE. YOU WILL FORGET I KNOW YOU

'''
#imports
#define class
class Pokemon: #the file name and the class name are spelled the same!!!

    #define global var
    
    #build your constructors-initial code
    def __init__(self,nickname,hp,species,level,p_type):
        self.nickname = nickname
        self.hp = hp
        self.species = species
        self.level = level
        self.p_type = p_type

    #build your getters and setters aka accessors and mutators
    
    #specific functions
    
    #toString
    def __str__(self):
        out= ""
        out += species+"\n"
        out += "\t"+nickname
        return f"{self.nickname} the {self.species}"

