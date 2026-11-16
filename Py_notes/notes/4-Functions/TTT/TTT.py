#import

#var
gameboard=[[" "," "," "],
           [" "," "," "],
           [" "," "," "]
        ]
#funct
def printboard(board):
    for r in range(3):
        print (f"{board[r][0]}|{board[r][1]}|{board[r][2]}")
        if r !=2:
            print("-"*5)
    print()
def userMove(player,board:
    print(f"It is {player}'s turn")
    row = int(input("row: "))-1
    col = int(input("col: "))-1
    if row in range(3) and col in range(3):
        if gameboard[row][col] == " ":
        gameboard[row][col]="X"






#check for winner
#   Vert
#   Horizantal
#   Diagonal

#check for cat

#mainloop
player ="X"             
while(player!="Q"):
    #draw board
    printboard(gameboard)
    #user goes
    userMove("x",gameboard)
    if player == "x":
             player="O"
    else:
             player="X"

printboard(gameboard)
#check for winner or cat

#gameover
print ("GG Mate")

