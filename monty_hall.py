# Import the random module
import random
# Create a function that simulates one Monty Hall game
def play_monty_hall(contestant_switches):
    # Create a list containing the three doors
    doors = [1,2,3]
    # Randomly choose which door contains the prize
    prize_door = random.choice(doors)
    # Randomly choose the contestant's door
    contestant_door = random.choice (doors)
    # Create a set that lists the doors Monty cannot open
    forbidden_doors = {prize_door, contestant_door}
    # Create an empty list for doors the host can open
    possible_doors = []
    # Check each door
    for door in doors:
        # If the door is not the prize door
        if door not in forbidden_doors:
        # Add it to the list of possible doors to open
             possible_doors.append(door)
    # Have the host randomly open one of the valid doors
    opened_door = random.choice(possible_doors)
    # If the contestant chooses to switch
    if contestant_switches:
        # Create a set for the forbidden doors when switching
        switch_forbidden_doors = {contestant_door, opened_door}
        # Find the one remaining unopened door
        for door in doors:
            # Switch to the only remaining unopened door
            if door not in switch_forbidden_doors:
                contestant_door = door
    # Check if the contestant's final choice matches the prize door
    if contestant_door == prize_door:
    # Return True if the contestant wins
        return True
    # Return False if the contestant loses
    else: 
        return False
# Create a variable to count wins when staying
stay_wins = 0
# Create a variable to count wins when switching
switch_wins = 0
# Choose how many games to simulate
total_games = 1000000
# Repeat for the desired number of games
for game in range(total_games):
    # Run one game where the contestant stays
    if play_monty_hall(False):
        # If the contestant wins, add one to the stay counter
        stay_wins += 1
    if play_monty_hall(True):
        #If the contestant wins, add one to the switch counter
        switch_wins += 1
# Display the total number of trials
print ("Total Games: ", total_games)
# Display the number of wins when staying
print ("Wins when staying: " , stay_wins)
# Display the win percentage when staying 
stay_win_percentage = stay_wins / total_games * 100
print("Win percentage when staying: ", stay_win_percentage)
# Display the number of wins when switching
print("Wins when switching: ", switch_wins)
# Display the win percentage when switching
switch_win_percentage = switch_wins / total_games * 100
print("Win percentage when switching: ", switch_win_percentage)
