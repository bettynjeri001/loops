# Write a short guessing game program using a while loop. The 
#user should be prompted to guess a number, and you should tell 
#them whether their guess was correct or wrong after each 
#guess. The loop should keeping running until the user guesses 
#the number correctly

target_number = 80
guess = int(input("Enter a number: "))
while guess != target_number:
    print("Wrong guess!")
    guess = int(input("Enter a number: "))
print("You guessed correctly!")