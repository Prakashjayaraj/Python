print("Welcome to my computer quiz")
score = 0
printing = input("Do you want to play the quiz? Yes/No ").lower()
if printing == "yes":
    print(printing)
else:
    print("I am not interested in playing the game.")
    quit()

print("Okay, let's play the game!")
question = input("CPU stands for? ").lower()
if question == "central processing unit":
    print("You are correct!")
    score += 1
else:
    print("Sorry, that's incorrect. Try again.")

print("Your score is " + str(score))  # Convert score to string before concatenating
percentage = (score / 1) * 100  # Calculate percentage
print("You got " + str(percentage) + "%")
