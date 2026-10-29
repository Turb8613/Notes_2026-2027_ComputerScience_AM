import string
import random
player= input("Rock(R) paper(P) scissors(S)").upper()

print(player)
rps_list =('R','P','S')
Pc = (random.choice(rps_list))
print(Pc)
if player == Pc :print(f"same choice {player} ")
elif player == ("R") and Pc == ("P"): print("PC wins")
elif player == ("P") and Pc == ("R"): print("Pc wins")
elif player == ("S") and Pc == ("P"): print("Player wins")
elif player == ("R") and Pc == ("S"): print("Player wins")
elif player == ("P") and Pc == ("S"): print("PC wins")
elif player == ("S") and Pc == ("R"): print("Player wins")
