#import

#var
gameboard=[[" "," "," "],
           [" "," "," "],
           [" "," "," "]
        ]

player= "X"
#funct

def printboard(board):
    for r in range(3):
        print (f"{board[r][0]}|{board[r][1]}|{board[r][2]}")
        if r !=2:
            print("-"*5)
    print()

def userMove(player,board):
    print(f"It is {player}'s turn")
    row = int(input("row: "))-1
    col = int(input("col: "))-1
    validSpot=False
    while(not validSpot):
        if (row in range(3) and col in range(3)):
            if board[row][col] == " ":
                validSpot=True
                break
            print("seat taken")
        print("invalid spot")
        row =int(input("row: "))-1
        col =int(input("col: "))-1
    board[row][col]=player






#check for winner
def checkForWinner(gameboard):
#   Horizantal
    for r in board:
       if r[0] == r[1] and r[1] == r[2] and r[0] != " ":
            print(f"Winner Winner Turkey Dinner {player} Won!")
            return True

#   Diagonal
    return False


def checkForCAT(board):
    for eachRow in board:
        for eachSpot in eachRow:
            if eachSpot == " ":
                return False
    print("CAT GAME!")
    return True
#check for cat

#mainloop
while(player!="Q"):
    #draw board
    printboard(gameboard)
    #user goes
    userMove(player,gameboard)
    #check for winner or cat
    if checkForCAT(gameboard):
        player = "Q"
        #swap turns
    if player == "X":
        player="O"
    else:
        player="X"
printboard(gameboard)
#gameover
print ("GG Mate")
printboard(gameboard)
