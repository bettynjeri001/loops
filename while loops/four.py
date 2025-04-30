# Write a short guessing game program using a while loop. The 
#user should be prompted to guess a number between 1 and 100, 
#and you should tell them whether their guess was too high or 
#too low after each guess. The loop should keeping running until 
#the user guesses the number correctly

target_number = 30
guess = int(input("Enter a number: "))
while guess != target_number:
    if guess > target_number:
        print("Guess Number given is Too high!")
    else:
        print("Guess Number given is Too low!")
    guess = int(input("Enter a number: "))
print("You guessed correctly!")