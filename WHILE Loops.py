import random 

# This program asks the user to guess a number between 1 and 10.
print ("Hello! this time you´re going to try guess a specific number, betwenn 1 and 10")
print ("Fun fact...it´s my favorite number!")
print ("Type your guess")

while True:
    G_NUMBER = random.randint(1,10)
    INVALID = 11
    guess = input("")
    if int(guess) < G_NUMBER:
        print ("Your guess is too low")
    if int(guess) > G_NUMBER:
        print ("Your guess is too high")
    if int(guess) == G_NUMBER:
        print ("Your guess is correct! Congratulations!")
    if int(guess) > INVALID:
        print ("Your guess is an invalid number") 
    
