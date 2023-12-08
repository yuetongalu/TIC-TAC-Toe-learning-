import time

def write_text(text,filename):
    """
    write the text into a file
    Input:
        text -> string
        filename -> The name of the file we want to write

    Output:
        none
    """

    #Open a file
    #file open modes: w -> write, r -> read, a -> append
    with open (filename,'a') as f:
        f.write(text+"\n") #\n ->new line
    

write_text("hellow, world","hello.txt")

play = [
    {
        "symbol": "X"
        "move_count":1
        "move": "2"
        "time_spend":6
    },
]

def dict_to_csv(data):
    """
    Input:
        data -> a dictionary
    Output:
        csv_str -> a valid csv row. i.e. 1, ian, uw
        """
    [str(x) for x in data.values()]

dict_to_csv({"name":"ian","score":123})



def ask_player_move(symbol):
    """
    Input:
        move -> Integer between 0 and 8
    Output:
        True if move success False is move is invalid
    """
    move_data = {}
    #time.time() -> current time in seconds
    move_start_time = time.time()
    move = input("Please enter a move, valid move is between 0 and 8:")
    move_done_time = time.time()

    move_data['symbol'] = symbol
    move_data['move'] = move
    move_data['duration_seconds'] = move_done_time - move_start_time

    print(move_data)
    csv_str = dict_to_csv()
    write_text_to_file(csv_str)

ask_player_move('X')


move_id= 1
game_data=[]

for x in range (10):

    num_of_move= random.dandint(5,9)
    game_id = time.time()
    move_id = 0
    for move in range (num_of_moves):
        move_id += 1
        duration = random (1,30)
        data['game_id'] = game_id
        data['move_id'] = move_id
        data['move_start_time']= data['move_start_time'] + duration
        data['duration'] = duration
        data['move'] = random.randint(0.9)
        if move_id == num_of_moves:
            data['is_winner'] = True
        else 
            data['is_winner']= False