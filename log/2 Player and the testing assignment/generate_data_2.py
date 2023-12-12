import csv
import random
import time


def categorize_move(row, col):
    """Categorize move position as corner, center, or middle."""
    if (row, col) in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        return 'corner'
    elif (row, col) == (1, 1):
        return 'center'
    return 'middle'

def simulate_game():
    game_id = time.time()
    symbols = ['X', 'O']
    num_moves = random.randint(5, 9)  
    first_move = random.choice([(r, c) for r in range(3) for c in range(3)])
    first_move_category = categorize_move(*first_move)
    game_winner = random.choice(symbols) if random.choice([True, False]) else None
    game_data = []

    for move_id in range(1, num_moves + 1):
        player_symbol = symbols[move_id % 2]
        move = first_move if move_id == 1 else random.choice([(r, c) for r in range(3) for c in range(3)])
        move_category = categorize_move(*move)

        move_data = {
            'game_id': game_id,
            'move_id': move_id,
            'player_symbol': player_symbol,
            'move_category': move_category,
            'first_move_category': first_move_category,
            'winner': player_symbol == game_winner if game_winner else 'draw'
        }

        game_data.append(move_data)

    return game_data

def write_to_csv(file_path, data):
    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ['game_id', 'move_id', 'player_symbol', 'move_category', 'first_move_category', 'winner']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerows(data)

def main():
    num_games = 30  # Number of games to simulate
    file_path = './game_data.csv'

    for _ in range(num_games):
        game_data = simulate_game()
        write_to_csv(file_path, game_data)

if __name__ == "__main__":
    main()
