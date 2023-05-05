import random

user_wins = 0
computer_wins = 0
options = ["pierre", "feuille", "ciseaux"]

while True:
    user_input = input("\nEcrit Pierre, Feuille ou Ciseaux ou Q pour quitter la partie ! ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    computer_option = options[random_number]
    print("\n-- L'ordinateur avait choisi :", computer_option + ".")

    if user_input == "pierre" and computer_option == "ciseaux":
        user_wins += 1
        print("-- Bravo !")
    elif user_input == "feuille" and computer_option == "pierre":
        user_wins += 1
        print("-- Bravo !")
    elif user_input == "ciseaux" and computer_option == "feuille":
        user_wins += 1
        print("-- Bravo !")
    elif user_input == computer_option:
        print("-- Match nul !")
    else:
        computer_wins += 1
        print("-- C'est perdu !")
    print(f"-- Ton score : {user_wins} || Ordinateur : {computer_wins}")

if user_wins == computer_wins and user_wins != 0:
    print(f"\nTu as fait {user_wins} points et l'ordinateur {computer_wins} points.")
    print("Vous êtes ex æquo !! Bravo !")
elif user_wins == 0 and computer_wins == 0:
    print(f"\nTu as fait {user_wins} points et l'ordinateur {computer_wins} points.")
    print("Dommage !!")
elif user_wins > 0 or computer_wins > 0:
    print(f"\nTu as fait {user_wins} points et l'ordinateur {computer_wins} points.")
    if user_wins > computer_wins:
        print("Bien joué ! :)")
    else:
        print("Encore une preuve que les ordinateurs dirigeront le monde..")

print("Merci d'avoir joué avec mon ordinateur !")