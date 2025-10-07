import random
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("The number of players has to be between 2 and 4 ")

    else:
        print("Invalid Input, try again")

max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:

    for player in range(players):
        print(f"\nPlayer {player + 1}'s turn\n")
        print("Your total score is ", players_score(player))
        current_score = 0

        while True:
             choice = input("Do you want to roll the dice(y): ")
             if choice.lower().strip() != "y":
                 break

             else:
                value = roll()
                if value == 1:
                    print("You rolled a 1! Turn done")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print("You rolled a ", value)

             print("Your score is ", current_score)

        players_score[player] += current_score
        print("Your total score is ", players_score[player])

winner = players_score.index(max(players_score))
print(f"\nThe max player score is {max(players_score)}. The winner is player {winner + 1}")