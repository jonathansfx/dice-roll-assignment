# python coin flip simulator
import random

# menu loop
loop = True
while loop:
# print menu 
    print("Dice Roll Simulator Menu")
    print("1. Roll Dice Once")
    print("2. Roll Dice 5 Times")
    print("3. Roll Dice 'n' Times")
    print("4. Roll Dice until Snake Eyes")
    print("5. Exit")

    
    selection = input("Select an option (1-5): ")
# selection
    if selection == "1":
        print("Option 1")
    elif selection == "2":
        print("Option 2")
    elif selection == "3":
        print("Option 3")
    elif selection == "4":
        print("Option 4")
    elif selection == "5":
        print("EXIT")
        loop = False