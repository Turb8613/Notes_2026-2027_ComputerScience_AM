#import
import ollama
import re

#var
gameboard=[[" "," "," "],
           [" "," "," "],
           [" "," "," "]
        ]
row = 0
col = 0
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
        row = int(input("row: "))-1
        col = int(input("col: "))-1
    board[row][col]=player

def aiMove(player, board):
    print(f"It is {player}'s turn (Ollama)...")
    
    free_spots = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                free_spots.append((r, c))

    if not free_spots:
        return
                
    prompt = (
        f"You are playing Tic-Tac-Toe as 'O'. The current board layout is:\n{board}\n"
       f"If you see a move that would let you win, take it. If the opponent is about to win, block them."
       f"If there are no immediate wins or blocks, pick a random available spot."
       f"be agressive and try to win"
       f"Respond with ONLY the row and column separated by a comma (e.g., 1,3). Do not say anything else."
       f"there are 3 rows and 3 columns, the top left is 1,1 and the bottom right is 3,3"
    )
    
    response = ollama.chat(
        model='llama3.2',
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.1}
    )
    content = response["message"]["content"]
    match = re.search(r"(?<!\d)([1-3])\s*,\s*([1-3])(?!\d)", content)
    if match:
        row, col = int(match.group(1)) - 1, int(match.group(2)) - 1
        if board[row][col] == " ":
            board[row][col] = player
            return

    print(f"AI returned an invalid move ({content!r}); choosing an available spot.")
    row, col = free_spots[0]
    board[row][col] = player

#check for winner
def checkForWinner(board):
    #check for hori winner
    for r in range(3):
        if(board[r][0] == board[r][1] and board[r][1] == board[r][2] and board[r][0] != " "):
            print("\n"*50)
            print("Winner winner, turkey dinner!")
            printboard(board)
            return True
    #check for vert winner
    for c in range(3):
        if(board[0][c] == board[1][c] and board[1][c] == board[2][c] and board[0][c] != " "):
            print("\n"*50)
            print("Winner winner, turkey dinner!")
            printboard(board)
            return True
    #check for diag winner
    if(board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " "):
        print("\n"*50)
        print("Winner winner, turkey dinner!")
        printboard(board)
        return True
    if(board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != " "):
        print("\n"*50)
        print("Winner winner, turkey dinner!")
        printboard(board)
        return True
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
    
    # Route turn based on who is playing
    if player == "X":
        userMove(player, gameboard)
    else:
        aiMove(player, gameboard)
        
    #check for winner or cat
    if checkForWinner(gameboard):
        player = "Q"
    elif checkForCAT(gameboard):
        player = "Q"
    elif player == "X":
        player="O"
    else:
        player="X"
        
printboard(gameboard)
#gameover
print ("GG Mate")
printboard(gameboard)
