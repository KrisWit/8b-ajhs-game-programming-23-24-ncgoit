# Hangman Game by Nevaeh Copeland, v0.9
import random
# words = 'game four five dark moon read eating camera button avenue emerge demand raining absolute mountain sentence children changes trumpet delivery repeated abbreviation television theatre living contemplating jeopardizing naivenesses confused supercalifragilisticexpialidocious'.split()
# DICTIONARY VERSION
# Stored in Key:Value Pairs.
# Actual Dictionary Word (Key): Value (Definition)
# Uses {} to specify a dictionary
words = {'Colors': 'red orange yellow green blue indigo violet fuschia teal garnet gold black white silver gold'.split(),
         'Animals': 'cat cow dog moose goose fish wombat wolverine giraffe hippoptamus lion alligater'.split(),
         'Shapes': 'square triangle circle rhombus parallelogram trapezoid diamond dodecahedron'.split(),
         'Foods': 'hamburger hotdog potato waffle pancake escargot oysters chips steak'.split()}

HANGMAN_BOARD = ['''
    +---+
        |
        |
        |
    =======''', '''
    +---+
    O   |
        |
        |
    =======''', '''
    +---+
    O   |
    |   |
        |
    =======''', '''
    +---+
    O   |
   /|   |
        |
    =======''', '''
    +---+
    O   |
   /|\  |
        |
    =======''', '''
    +---+
    O   |
   /|\  |
   /    |
    =======''', '''
    +---+
    O   |
   /|\  |
   / \  |
    =======''', '''
    +---+
    O   |
  o-|-o |
   / \  |
    =======''', '''
    +---+
    O   |
  o-|-o |
   / \  |
  o   o |
    =======''']

# Pick Word from list
# def getRandomWord(wordList): # Return a random word from the list
#     wordIndex = random.randint(0, len(wordList) - 1)
#     # len(listName) -1 is EXTREMELY COMMON FOR WORKING WITH LISTS.
#     return wordList[wordIndex]

# Pick Word from Dictionary
def getRandomWord(wordDict): # Return a random word from the list
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0,len(wordDict[wordKey]) - 1 )
    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard (missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print()

    blanks = '_' * len(secretWord)

    # Replace Blanks with Correct Letters
    for i in range (len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks [:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed):
    while True:
        print('Please guess a letter and press enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('Letter as been guessed already, try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please guess a LETTER from the English alphabet.')
        else:
            return guess

def playAgain():
    print('Do you want to play again? Yes or No?')
    return input().lower().startswith('y')

# Introduce the Game
print('Welcome to Hangman created by Nevaeh C.')

# CHOOSE DIFFICULTY
difficulty = 'X'
while difficulty not in 'EMH':
    print('Please Choose Easy, Medium or Hard. Type the first letter then press enter.\n')
    difficulty = input().upper()
if difficulty == 'M': # MEDIUM
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
if difficulty == 'H': # HARD
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
    del HANGMAN_BOARD[5]
    del HANGMAN_BOARD[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

# Main Game Loop
while True:
    print('The secret word is from the ' + secretSet + ' categroy.\n')
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check To See If Winner, Winner Chicken Dinner
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters: # if True
            print('Dang you got me :( but W mans!')
            print('The secret word was ' +  secretWord)
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_BOARD) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out og guesses and lost the game.')
            print('You made this number of correct guesses ' + str(len(correctLetters)))
            print('The secret word was ' + secretWord)
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break

