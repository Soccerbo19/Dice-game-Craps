import random
print("Welcome to the Dice Game!")
play = input("Do you want to play? (yes/no): ").lower()

def roll_dice():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        return dice1, dice2, total
def play_game():
    dice1, dice2, total = roll_dice()
    print(f"You rolled a {dice1} and a {dice2}. Total: {total}")
    if total == 7 or total == 11:
        print("You win!")
    elif total == 2 or total == 3 or total == 12:
        print("You lose!")
    else:
        point = total
        print(f"Your point is {point}.")
        while True:
            dice1, dice2, total = roll_dice()
            print(f"You rolled a {dice1} and a {dice2}. Total: {total}")
            if total == point:
                print("You win! You matched your point.")
                    break
            elif total == 7:
                print("You Lose! You rolled a 7 before matching your point.")
                break

if play == "yes":
     play_game()
else:

     print("Okay see you next time!")
