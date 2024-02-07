# Dice roll assignment
import random
loop = True
while loop:
# print menu
    print("\nDice Roll Simulator Menu ")
    print("1. Roll Dice Once")
    print("2. Roll Dice 5 Times")
    print("3. Roll Dice 'n' Times")
    print("4. Roll Dice until Snake Eyes")
    print("5. Exit")
    selection = input("Select an option (1-5): ")

# selector
    if selection == "1":
        print("\nRoll Dice Once")
        randNum1 = random.randint(1,6)
        randNum2 = random.randint(1,6)
        sum = randNum1 + randNum2
        print(f"{randNum1},{randNum2} (sum: {sum})")
    elif selection == "2":
        print("\nRoll Dice 5 Times")
        n = 1
        while n < 6:
            randNum1 = random.randint(1,6)
            randNum2 = random.randint(1,6)
            sum = randNum1 + randNum2
            print(f"{randNum1},{randNum2} (sum: {sum})")
            n += 1
    elif selection == "3":
        print("Roll Dice 'n' Times")
        n = input("Enter how many times you would like to roll: ")
        i = 0
        while i < int(n):
            randNum1 = random.randint(1,6)
            randNum2 = random.randint(1,6)
            sum = randNum1 + randNum2
            print(f"{randNum1},{randNum2} (sum: {sum})")
            i += 1
    elif selection == "4":
        print("\nRoll Dice until Snake Eyes")
        n = 0
        loop = True
        while loop:
            randNum1 = random.randint(1,6)
            randNum2 = random.randint(1,6)
            sum = randNum1 + randNum2
            print(f"{randNum1},{randNum2} sum:{sum}")
            n += 1
            if sum == 2:
                print(f"SNAKE EYES!!!! it took you {n} rolls")
                loop = False
    elif selection == "5":
        print("EXIT")
        loop = False
