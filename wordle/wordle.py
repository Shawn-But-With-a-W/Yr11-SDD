class Wordle:
    def __init__(self):
        pass

    def getGuess(self, words):
        valid = False
        
        while valid == False:
            guess = input('\n Guess: ')

            if guess in words:
                valid = True
            else:
                print('Invalid guess.')

        else:
            return guess


    def checkGuess(self, word, guess):
        if word == guess:
            correct = True

        else:
            correct = False
            
            for i in range(5):
                if guess[i] == word[i]:
                    print(f'{guess[i]} is in the right position.')
                elif guess[i] in word:
                    print(f'{guess[i]} is in the wrong position.')
                else:
                    print('Invalid guess.')

        return correct


    def endGame(self, word, won, count):
        print('')
        
        if won:
            print(f'You guessed the word in {count} guesses!')
        else:
            print(f'You lost. The word was {word}.')
        

