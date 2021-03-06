# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
# print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock

# Solution:

while True:
    player_1 = input('Player 1: \n Rock-Papers-Scissors ?: ')
    player_2 = input('Player 2: \n Rock-Papers-Scissors ?: ')
    if player_1 == player_2:
        print("It's a tie, play again")
    elif player_1 == 'rock' and player_2 == 'scissors':
        print('Congratulations to player 1')
    elif player_1 == 'scissors' and player_2 == 'rock':
        print('Congratulations to player 2')
    elif player_1 == 'scissors' and player_2 == 'paper':
        print('Congratulations to player 1')
    elif player_1 == 'paper' and player_2 == 'scissors':
        print('Congratulations to player 2')
    elif player_1 == 'paper' and player_2 == 'rock':
        print('Congratulations to player 1')
    elif player_1 == 'rock' and player_2 == 'paper':
        print('Congratulations to player 2')
    else:
        print('Invalid input!')
    if input('Do you want to play again ? (y/n): ') == 'n':
        break
        
# Solution 2:

while True:
    player_1 = input('Player 1: \n Rock-Papers-Scissors ?: ')
    player_2 = input('Player 2: \n Rock-Papers-Scissors ?: ')
    if player_1 == player_2:
        print("It's a tie, play again")
    elif player_1 == 'rock' and player_2 == 'scissors' or player_1 == 'scissors' and player_2 == 'paper' or player_1 == 'paper' and player_2 == 'rock':
        print('Congratulations to player 1')
    elif player_1 == 'scissors' and player_2 == 'rock' or player_1 == 'paper' and player_2 == 'scissors' or player_1 == 'rock' and player_2 == 'paper':
        print('Congratulations to player 2')
    else:
        print('Invalid input!')
    if input('Do you want to play again ? (y/n): ') == 'n':
        break

