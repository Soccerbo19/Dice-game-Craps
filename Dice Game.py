import random

print("Welcome to the Dice Game!")
rules = print("The rules are simple." \
"Roll the dice and try to get a sum of 7 or 11 on your first roll to win. " \
"If you roll a 2, 3, or 12, you lose. " \
"If you roll any other number, that becomes your point. You then keep rolling until you either match your point to win or roll a 7 to lose.")

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    return dice1, dice2, total

def play_game(player_number):
    print(f"\n🎲 Player {player_number}'s turn")

    dice1, dice2, total = roll_dice()
    print(f"You rolled a {dice1} and a {dice2}. Total: {total}")

    if total == 7 or total == 11:
        print("You win on the come-out roll!")
        return True

    elif total == 2 or total == 3 or total == 12:
        print("You lose on the come-out roll!")
        return False

    else:
        point = total
        print(f"Your point is {point}.")

        while True:
            dice1, dice2, total = roll_dice()
            print(f"You rolled a {dice1} and a {dice2}. Total: {total}")

            if total == point:
                print("You win! You matched your point.")
                return True

            elif total == 7:
                print("You lose! You rolled a 7 before matching your point.")
                return False

while True:
    play = input("\nDo you want to play? (yes/no): ").lower()

    if play != "yes":
        print("Okay see you next time!")
        break

    players = int(input("How many players are playing? "))

    for player in range(1, players + 1):

        play_game(player)
