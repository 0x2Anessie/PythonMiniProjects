print("Hello World ! Welcome to my quizz")

playing = input("Are you ready ? ")
if playing.lower() != "yes":
    quit()
else:
    print("Okay! :) Let's Play !")

score = 0

answer = input("First question : What does RAM stand for ? ")
if answer.lower() == "random access memory":
    print("\nCorrect!")
    score += 1
else:
    print("\nIncorrect")

answer = input("Second question : What does == mean ? ")
if answer.lower() == "equal":
    print("\nCorrect!")
    score += 1
else:
    print("\nIncorrect")

answer = input("Third question : What does && mean ? ")
if answer.lower() == "and":
    print("\nCorrect!")
    score += 1
else:
    print("\nIncorrect")

answer = input("Fourth question : What does || mean ? ")
if answer.lower() == "or":
    print("\nCorrect!")
    score += 1
else:
    print("\nIncorrect")

if score <= 1:
    print("You got " + str(score) + " question correct that is " + str((score / 4) * 100) + "%")
else:
    print("You got " + str(score) + " questions correct that is " + str((score / 4) * 100) + "%")

if score > 2 or score == 2:
    print("Well done :)")
else:
    print("Hope you'll do better next time :(")