import random

def roll2Dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"{die1},{die2} (sum: {total})")

def menu():
    loop = True
    while loop:
        print("\nDice Roll Simulator Menu")
        print("1. Roll Dice Once")
        print("2. Roll Dice 5 Times")
        print("3. Roll Dice 'n' Times")
        print("4. Roll Dice until Snake Eyes")
        print("5. Exit")
        
        selection = input("Select an option (1-5): ")

        if selection == "1":
            print("\nRoll Dice Once")
            roll2Dice()
        elif selection == "2":
            print("\nRoll Dice 5 Times")
            for _ in range(5):
                roll2Dice()
        elif selection == "3":
            print("\nRoll Dice 'n' Times")
            num_rolls = int(input("How many rolls would you like? "))
            for _ in range(num_rolls):
                roll2Dice()
        elif selection == "4":
            print("\nRoll Dice until Snake Eyes")
            rolls = 0
            while True:
                rolls += 1
                total = roll2Dice()
                if total == 2:
                    print(f"SNAKE EYES! It took {rolls} rolls to get snake eyes.")
                    break
        elif selection == "5":
            print("Exiting program...")
            loop = False
        else:
            print("Invalid selection. Please choose a number from 1 to 5.")

