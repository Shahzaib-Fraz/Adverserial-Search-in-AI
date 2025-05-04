import math

# Initialize a 3x3 Tic-Tac-Toe board with empty spaces.
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
nodes_explored=0
def print_board(board):
    """prints current state of board """
    print("\n".join([" | ".join(row)for row in board]) + "\n")

def is_winner(board, player):
    """checks the given player has won or not ., return true , false """
    
    # for rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # for columns
    for col in range(len(board[0])):
        if all(board[row][col] == player for row in range(len(board))):
            return True

    # for  diagonal (\)
    if all(board[i][i] == player for i in range(len(board))):
        return True

    # for second diagonal (/)
    if all(board[i][len(board) - 1 - i] == player for i in range(len(board))):
        return True

    return False  


def is_full(board):
    """returns True if the board is full else false"""
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing,ai_player,human_player,alpha,beta):
    """ Minimax algorithm to evaluate board positions two option ,set depth level heuristic ,or 
    continue till game end ,return best score  """
    global nodes_explored
    nodes_explored +=1
    if is_winner(board, ai_player):  # AI wins
        return 1
    if is_winner(board, human_player):  # Human wins
        return -1
    if is_full(board):  # Tie
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = ai_player
                    eval = minimax(board, depth + 1, False, ai_player, human_player, alpha, beta)
                    board[i][j] = ' '  # Undo move
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:  # Alpha-Beta pruning condition
                        break  # Prune remaining branches
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = human_player
                    eval = minimax(board, depth + 1, True, ai_player, human_player, alpha, beta)
                    board[i][j] = ' '  # Undo move
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:  # Alpha-Beta pruning condition
                        break  # Prune remaining branches
        return min_eval 

def best_move(board,ai_player,human_player):
    """finds and returns the best move for the AI using the minimax function."""
    max_score=-float('inf')
    move=None
    alpha=-float('inf')
    beta=float('inf')
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                board[i][j] = ai_player
                score=minimax(board,0,False,ai_player,human_player,alpha,beta)
                board[i][j] =" "
                if score > max_score:
                    max_score=score
                    move=(i,j)
    return move

def main():
    """Main game loop."""
    # print(is_winner(board,"1"))
    ai_player="X"
    human_player="O"
    print_board(board)
    
    for _ in range(9):  # Max 9 moves in Tic-Tac-Toe
        # Human player move
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column 0-2): ").split())
                if board[row][col] == ' ':
                    board[row][col] = human_player
                    break
                else:
                    print("Cell occupied, try again.")
            except (ValueError, IndexError):
                print("Invalid input, enter row and column between 0-2.")
        
        print_board(board)
        if is_winner(board, human_player):
            print("You win!")
            return
        if is_full(board):
            print("It's a tie!")
            return
        
        # AI move
        print("AI is thinking...")
        move = best_move(board, ai_player, human_player)
        if move:
            board[move[0]][move[1]] = ai_player
        
        print_board(board)
        if is_winner(board, ai_player):
            print("AI wins!")
            return
        if is_full(board):
            print("It's a tie!")
            return
main()
print(nodes_explored)