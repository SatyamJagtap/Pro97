import random

print('Number Guessing Game')

num = random.randint(1,9)

chance = 0

print('I have guessed any one number from 1 to 9. Can you find it?')

while chance <5:
    guess = int(input("Enter you guess"))

    if guess == num:

        print('Congratulation You Won!')

    elif guess < num:
        print('Guess a higher number than', guess)

    else:
        print("Guess a lower number than", guess)


chance +=1

if chance == 5:
    print("You Lose! The number was", num)