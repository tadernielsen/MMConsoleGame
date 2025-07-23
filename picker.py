import numpy as np
import random as rnd
from user import user

def CreateUser(name):
    return user(name)

def calculateTotalChance(users):
    totalChance = 0

    for user in users:
        totalChance += user.chance
    
    return totalChance

def calculateIndividualChance(user, totalChance):
    if totalChance <= 1:
        raise ValueError("Not enough players")
    return (user.chance / totalChance)

def game(users):
    maxTurns = 30
    pass

def main():
    users = []
    totalChance = 0

    print("Welcome!\n")

    while True:
        print("Menu:")
        print("1. Create new user")
        print("2. Remove user")
        print("3. Check Muderer Chances")
        print("4. Start game")
        print("5. Exit")
        print()

        choice = input("> ")

        if choice == '1':
            if len(users) == 16:
                print("Maximum number of users reached (16).\n")
                continue

            name = input("Enter user name: ")
            users.append(CreateUser(name))
            print(f"User '{name}' created.\n")
        elif choice == '2':
            pass
        elif choice == '3':
            totalChance = calculateTotalChance(users)
            
            for user in users:
                chance = calculateIndividualChance(user, totalChance) * 100
                print(f"{user.name}: {chance:.1f}%")
            print()
            
        elif choice == '4':
            pass
        elif choice == '5':
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()