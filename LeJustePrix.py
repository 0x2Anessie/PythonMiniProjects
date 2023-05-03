print("Bienvenue au juste prix !!")

playing = input("Tu veux commencer le jeu ? ")
if playing.lower() != "oui":
    quit()
else:
    print("\nSuper !! Aujourd'hui on va deviner le prix d'un siège gaming Herman Miller.")
    print("Pour les experts le modèle exacte s'appelle Aeron ;)\nCommençons !")

price = 1725
guesses = 0

while True:
    guesses += 1
    user_guess = input("Selon toi combien coute ce siège ? ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print("Écrit un nombre la prochaine fois !")
        continue

    if user_guess <= 0:
        print("Un siège gratuit c'est peu réaliste !")

    if user_guess == price:
        print("\nBravo !! Le siège Herman Miller vaut bien 1725 euros !")
        break
    elif user_guess > price:
        print("\nC'est un peu trop cher..")
    else:
        print("\nC'est pas assez cher..")

print("Tu as trouvé le juste prix en", guesses, "coups.")