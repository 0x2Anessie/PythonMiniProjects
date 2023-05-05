import random

user_wins = 0
computer_wins = 0
options = ["pierre", "feuille", "ciseaux"]

while True:
    user_input = input("Ecrit Pierre, Feuille ou Ciseaux ou Q pour quitter la partie ! ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    computer_option = options[random_number]
    print("\nL'ordinateur avait choisi :", computer_option + ".")

    if user_input == "pierre" and computer_option == "ciseaux":
        print("Bravo !")
        user_wins += 1
    elif user_input == "feuille" and computer_option == "pierre":
        print("Bravo !")
        user_wins += 1
    elif user_input == "ciseaux" and computer_option == "feuille":
        print("Bravo !")
        user_wins += 1
    elif user_input == computer_option:
        print("Match nul !")
    else:
        print("C'est perdu !")
        computer_wins += 1

if user_wins > 0 and computer_wins > 0:
    print("\nTu as gagné", user_wins, "fois et l'ordinateur a gagné", computer_wins, "fois.")
    if user_wins > computer_wins:
        print("Bien joué ! :)")
    else:
        print("Encore une preuve que les ordinateurs dirigeront le monde..")

print("\nAdios !")