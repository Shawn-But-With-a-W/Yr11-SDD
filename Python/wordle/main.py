from wordlist import words
from wordle import Wordle
from random import choice

wordle = Wordle()

word = choice(words)

# print(word)

for count in range(5):
    guess = wordle.getGuess(words)

    won = wordle.checkGuess(word, guess)

    if won:
        break

wordle.endGame(word, won, count+1)