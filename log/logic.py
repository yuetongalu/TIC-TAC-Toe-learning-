def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # If no winner, check for a draw
    if all(cell != ' ' for row in board for cell in row):
        return 'Draw'



    # Check Board FUll 
    flat_board = []
    for row in board:
        flat_board.extend(row)
    if not "_" in flat_board:
        return "draw" 
    
    return None

    
if __name__ == "__main__":
    board = [
        ["O","X","O"],
        ["O","O","X"],
        ["X","X","O"],
    ]
    print(check_winner(board))