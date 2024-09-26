# Function to read players from a file
def read_players_from_file(filename):
    with open(filename, 'r') as file:
        players = [line.strip() for line in file.readlines()]
    return players

# Read players from the file
players = read_players_from_file('players.txt')

# Counter to keep track of the current position in the list
current_position = 0

def select_goalies():
    global current_position
    # Select two players starting from the current position
    goalie1 = players[current_position]
    goalie2 = players[(current_position + 1) % len(players)]
    
    # Print the names of the selected players
    print(f"Selected Goalies: {goalie1}, {goalie2}")
    
    # Update the counter to the next position, wrapping around if necessary
    current_position = (current_position + 2) % len(players)

# Example usage
for _ in range(5):  # Rotate through the list a few times
    select_goalies()