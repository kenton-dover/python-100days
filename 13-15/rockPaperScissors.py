from hands import Rolls
from people import Player
import random


def get_player_roll():
    return input("Enter [R]ock [P]aper or [S]cissors: ")


def game_loop(player1, player2, rolls):
    count = 1
    while count < 3:
        p2_roll = random.choice(rolls)  # TODO: get random roll
        p1_roll = get_player_roll()  # TODO: have player choose a roll
        if p1_roll is 'R':
            p1_roll = rolls[0]
        elif p1_roll is 'P':
            p1_roll = rolls[1]
        else:
            p1_roll = rolls[2]
        outcome = p1_roll.can_defeat(p2_roll)

        # display throw
        print(
            f"Player threw a {p1_roll.name} and computer threw a {p2_roll.name}")
        if outcome is None:
            print("Throw is a draw")
        elif not outcome:
            print(f"{player2.name} has won the throw")
            player2.winning += 1
        elif outcome:
            print(f"{player1.name} has won the throw")
            player1.winning += 1

        count += 1

    # Compute who won
    if player1.winning > player2.winning:
        print(f"{player1.name} has won")
    elif player1.winning < player2.winning:
        print(f"{player2.name} has won")
    else:
        print("It is a draw")


def build_the_three_rolls():
    listOfRolls = []
    listOfRolls.append(Rolls("Rock", ["Scissors"], ["Paper"]))
    listOfRolls.append(Rolls("Paper", ["Rock"], ["Scissors"]))
    listOfRolls.append(Rolls("Scissors", ["Paper"], ["Rock"]))
    return listOfRolls


def print_header():
    print("---------------------------------")
    print("       Rock Paper Scissors       ")
    print("---------------------------------")
    print()


def get_players_name():
    return input("Please enter your name: ")


def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name, 0)
    player2 = Player("computer", 0)

    game_loop(player1, player2, rolls)


if __name__ == '__main__':
    main()
