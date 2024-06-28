import random
import os
import time

def initialize_game_board(width, height):
    # Create an empty game board with the given dimensions
    return [['.' for _ in range(width)] for _ in range(height)]

def generate_targets(target_count, width, height):
    # Generate and return a list of target positions with the given parameters
    targets = []
    while len(targets) < target_count:
        x = random.randint(0, width-1)  # Ensure targets are within the board
        y = random.randint(0, height-1)
        if [x, y] not in targets:
            targets.append([x, y])
    return targets

def print_game_board(game_board, player_position, targets):
    # Print the game board with player position and targets
    for y in range(len(game_board)):
        for x in range(len(game_board[y])):
            if [x, y] == player_position:  # Player position
                print('P', end='')
            elif [x, y] in targets:  # Target position
                print('G', end='')
            else:
                print('.', end='')  # Empty space
        print()

# Board dimensions
width = 10
height = 5

# Number of targets
target_count = 5

game_board = initialize_game_board(width, height)
# Players 1 and 2
players = ['Player 1', 'Player 2']
times = [0, 0]  # Times will be recorded as floats
targets_found = [0, 0]  # Number of targets found

for player in players:  # player is the index of players [0] and [1]

    player_position = [0, 0]  # Initial player position
    targets = generate_targets(target_count, width, height)  # Generate targets with count, height, and width
    print(f"Turn: {player}")
    input("Press Enter to start the game...")
    start_time = time.time()  # Timer to count how long the player is playing

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen and check the operating system
        print_game_board(game_board, player_position, targets)

        n = input()  # User input
        
        # Change player position based on user input
        if n == 'w' and player_position[1] > 0:
            player_position[1] -= 1
        elif n == 's' and player_position[1] < height-1:
            player_position[1] += 1
        elif n == 'a' and player_position[0] > 0:
            player_position[0] -= 1
        elif n == 'd' and player_position[0] < width-1:
            player_position[0] += 1
        
        # Check if the player is at a target position, if so, remove it and update the count
        if player_position in targets:
            targets.remove(player_position)
            targets_found[players.index(player)] += 1
        
        # Check the number of targets found
        if targets_found[players.index(player)] == target_count:
            end_time = time.time()
            times[players.index(player)] = end_time - start_time
            print(f"{player} has won! Time: {times[players.index(player)]:.2f} seconds.")
            break

# Check and print the game result
if times[0] < times[1]:
    print()
    print("Player 1 has won, they had the better time!")
elif times[0] > times[1]:
    print()
    print("Player 2 has won, they had the better time!")
else:
    print()
    print("It's a tie! Both players have the same time!")
