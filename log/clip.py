from logic import check_winner

def get_empty_board():
    return[
        [None,None,None],
        [None,None,None],
        [None,None,None]
    ]

def print_board(board):
    for row in board:
        print(row)

def get_player_input(current_player):
    """
    return:
        row: int-> the index of row
        col: int-> the index of column
    """
    prompt = f"player {current_player} > "
    player_input = input(f">") #this is a str
        
    row_col_list = player_input.split(',')   
    row,col = [int(x) for x in row_col_list]
    print(row,col)
    return row, col

#how to make str into two int

def switch_player(current_player):
    if current_player == 'X':
        return 'O'
    return 'X'
    
if __name__ == '__main__':
    current_player = "X"
    #get a empty board
    board = get_empty_board()
    winner = None

    while winner is None:
         print_board(board)
         try:
                row, col =get_player_input(current_player)
         except ValueError:
                print("Invalid input, try again")
                continue
         if row >= len(board) or col >= len(board):
              print("You place something out of the board,try again")
              continue
        #  except IndexError:
        #         print("You place something out of the board,try again")
        #         continue



        #row,col = get_player_input(current_player)
         print(row)
         print(current_player)
         board [row][col] = current_player
         winner = check_winner(board)
         print("Winner is ", winner)
         current_player =switch_player(current_player)

         #print_board(board)
