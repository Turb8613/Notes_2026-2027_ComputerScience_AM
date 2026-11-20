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
def checkForWinner(board):
    #check for hori winner
    for r in range(3):
        if(board[r][0] == board[r][1] and board[r][1] == board[r][2] and board[r][0] != " "):
            print("\n"*50)
            print("Winner winner, turkey dinner!")
            printBoard(board)
            return True
    #check for vert winner
    for c in range(3):
        if(board[0][c] == board[1][c] and board[1][c] == board[2][c] and board[0][c] != " "):
            print("\n"*50)
            print("Winner winner, turkey dinner!")
            printBoard(board)
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
