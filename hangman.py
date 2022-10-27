# Joshua Michaelson 
# Start Time: 2:53pm 
# Code Challenge – Hangman  
# The Problem  
# Create a game of hangman  

import random
def main():
    # start game 
    print("Welcome to terminal Hangman! ")
    keepPlaying = input("Would you like to play? (yes/no) \n")
    keepPlaying = keepPlaying.lower()
    # function that allows user to play hangman
    def hangman():
        # create word list
        wordList = ['infallable', 'inconceivable', 'communistic', 'harambe', 'academic', 'fortification', 'senseless', 'tripthong','knapsack', 'xenotransplantation']
        #randomly select word
        randNum = random.randrange(0, len(wordList))
        gameWord = wordList[randNum]
        gameWord = list(gameWord)
        wordLen = len(gameWord)
        #display characters
        print(f"Ok! The word has {wordLen + 1} characters! ")
        # guess word to keep track of user progress
        guessWord = []
        for i in range(0, wordLen, 1):
            guessWord.append("_")
        print("".join(guessWord))
        # initialize guess numbers
        numGuesses = 0
        numCorrectGuesses = 0
        numWrongGuesses = 0 
        wrongGuesses = []
        # keep user guessing until word is guessed or they quit >:)
        while guessWord != gameWord:
            guess = input("What letter would you like to guess? \n(or type \'stop\' to end game)\n")
            # add break condition 
            if guess.lower() == "stop":
                break
        #begin guess routine
            numGuesses += 1
            # loop checks if guess matches any character in the word and updates guessword
            for char in range(0, wordLen, 1):
                if guess == gameWord[char]:
                    guessWord[char] = guess
            # triggers correct guess response   
            if guess in gameWord:
                numCorrectGuesses += 1
                print("Congratulations! That letter was in the word!")
                print("Here is the word now:")
                print("".join(guessWord))
            # triggers incorrect guess response
            if guess not in guessWord:
                numWrongGuesses += 1
                wrongGuesses.append(guess)
                print("Sorry, that letter isn't in the word")
                print("Here is what you have guessed so far:")
                print("".join(guessWord))
                print("Here are your previous guesses:")
                print(wrongGuesses) 
            # displays if user guessed the word
            if ''.join(guessWord) == ''.join(gameWord):
                print("Congratulations! You guessed the word!")
                print(''.join(gameWord))
            print(f"You have made {numGuesses} guesses, {numCorrectGuesses} correct guesses and {numWrongGuesses} wrong guesses")
        
    # determine if user wants to continue
    while keepPlaying == "yes":
        hangman()
        keepPlaying = input("Would you like to play again? (yes/no) \n")
        keepPlaying = keepPlaying.lower()
    print("Thanks for playing!")

main()

# Finished at 4:09pm
