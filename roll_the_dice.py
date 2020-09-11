import random

is_roll_again = ""

while True:

    random_numbers = random.randint(1, 6)
    random_numbers2 = random.randint(1, 6)
    if is_roll_again.lower() == "yes" or is_roll_again.lower() == "y":
        print("Rolling the dice..")
        print(f"---Numbers are {random_numbers}, {random_numbers2}")
        is_roll_again = input("Do you want to roll the dice again? : ")
    elif is_roll_again.lower() == "quit" or is_roll_again.lower() == "no":
        quit()
    else:
        print("---Use \"yes\" and \"y\" to play, or \"no\" and \"quit\" to terminate!")
        is_roll_again = input("Do you want to roll the dice again? : ")
