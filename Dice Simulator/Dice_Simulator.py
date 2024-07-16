import random


def randomizer():
    randomNumber = random.randint(1, 6)
    return randomNumber


def simulation():
    ranNum = randomizer()

    if ranNum == 1:
        print(" ┌─────────┐\n",
              "│         │\n",
              "│    ●    │\n",
              "│         │\n",
              "└─────────┘\n")
    elif ranNum == 2:
        print(" ┌─────────┐\n",
              "│  ●      │\n",
              "│         │\n",
              "│      ●  │\n",
              "└─────────┘\n")
    elif ranNum == 3:
        print(" ┌─────────┐\n",
              "│  ●      │\n",
              "│    ●    │\n",
              "│      ●  │\n",
              "└─────────┘\n")
    elif ranNum == 4:
        print(" ┌─────────┐\n",
              "│  ●   ●  │\n",
              "│         │\n",
              "│  ●   ●  │\n",
              "└─────────┘\n")
    elif ranNum == 5:
        print(" ┌─────────┐\n",
              "│  ●   ●  │\n",
              "│    ●    │\n",
              "│  ●   ●  │\n",
              "└─────────┘\n")
    elif ranNum == 6:
        print(" ┌─────────┐\n",
              "│  ●   ●  │\n",
              "│  ●   ●  │\n",
              "│  ●   ●  │\n",
              "└─────────┘\n")


def option(choice1):
    if choice1 == "y":
        simulation()
    else:
        print("Thank You! for using Dice Simulator.")
        quit()


print("Welcome To Dice Simulator!")

while True:
    choice = input("Do you want to spin the Dice (y/n)? ").lower()
    if choice in ('y', 'n'):
        option(choice)
    else:
        print("Invalid input, Please choose only (y/n)")
