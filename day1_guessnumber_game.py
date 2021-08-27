import random

secret = random.randint(1, 20)
print(secret)

for i in range(1, 7):
    guess = input("Enter a number between 1 and 20: ")
    guess = int(guess)
    
    if guess == secret: 
        print("right guess")
        print("number of try is " + str(i))
        break
    elif guess > secret:
        print("your guess is too high")
    else:
        print("Your guess is too low")
    
print("End of Program")