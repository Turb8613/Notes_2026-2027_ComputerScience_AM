#import
import ollama

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
        row = int(input("row: "))-1
        col = int(input("col: "))-1
    board[row][col]=player

def aiMove(player, board):
    print(f"It is {player}'s turn (Ollama)...")
    
    # Track open spots to tell the AI what its options are
    free_spots = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                free_spots.append(f"{r+1},{c+1}")
                
    prompt = (
        f"You are playing Tic-Tac-Toe as 'O'. The current board layout is:\n{board}\n"
        f"Pick one empty spot from this list: {free_spots}. "
        "If you see a move that would let you win, take it. If the opponent is about to win, block them. "
        "If there are no immediate wins or blocks, pick a random available spot."
        "be agressive and try to win,"
        "Respond with ONLY the row and column separated by a comma (e.g., 1,3). Do not say anything else."
    )
    
    try:
        response = ollama.chat(
            model='gemma4:31b',
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0.1}
        )
        # Parse out the row and column numbers from the response
        digits = [int(x) for x in response['message']['content'] if x.isdigit()]
        row, col = digits[0] - 1, digits[1] - 1
    except:
        # Fallback to the first available spot if the AI breaks character or fails
        row, col = [int(x) - 1 for x in free_spots[0].split(',')]

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
