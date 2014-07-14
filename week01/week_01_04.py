#import random module
import random

#creating variable and getting random number (within 1-100) into this var
greatNumber = random.randint(1, 100)

#creating variable that is close to previous random number
nearGreat = random.randint((greatNumber - 3),(greatNumber + 3))
#changin it if it is the same number
if (nearGreat == greatNumber):
    nearGreat += 1
    
#asking user to enter number and converting it to integer.
print ("Guess number from 1 to 100.\nIf you will guess right I give you answer to life, the universe and everything.\n(Additional information for cheaters: magic number somewhere near",nearGreat,")\nReady? Let's play:")

#creating variabl to check if the game is over and variable to count how many times user tried to guess
gameOver = 0
userTries = 0
while (gameOver == 0):


    userGuess = input()

    #creating counter for tries and adding 1 everytime
    userTries += 1

    #verify that it is a positive number
    if (userGuess.isdigit()):

        #converting string to integer
        userGuess = int(userGuess)

        #checking if number is in range
        if (userGuess >= 1 and userGuess <= 100):
        
            if (userGuess > greatNumber):
                print ("Too big. Try again:")
            elif (userGuess < greatNumber):
                print ("Nop. Try bigger number:")
            else:
                if (userTries == 1):
                    print ("You guessed it after just 1 try! So fast! So much luck! Wow!... Cheater.")
                    gameOver = 1
                elif (userTries <= 3):
                    print ("Congratulations! You've guessed it after", userTries, "tries!\nThe answer to life, the universe and everything is 42.\nThat's it. Move along. Nothing to see here.")
                    gameOver = 1
                elif (userTries > 3): #restart the game if user guessed with more than 3 tries
                    print ("Finally. After", userTries, "tries... Not sure if you are the one to share my secret.\nLet's play again:")
                    greatNumber = random.randint(1, 100) #setting another random number
                    userTries = 0 #reseting how many times user tried to guess
                    nearGreat = random.randint((greatNumber - 1),(greatNumber + 1))#Narrowing the range of help
                    if (nearGreat == greatNumber):
                        nearGreat += 1
                    
                    print ("Cheater, cheater, pumpkin eater. Here is some info for you.\nThe number is very close to",nearGreat) 
        else:
            print ("Use numbers from 1 to 100. Let's try again:")
            
    else:
        print ("I told you to enter a positive number number. Not some nonsense.")
        gameOver = 1 #if user enter not a positive number the game is over 
        
else:
    print ("Game Over")

