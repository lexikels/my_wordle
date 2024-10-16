#imports
import random
import string

WORD_FILE = 'english_words.txt'
#generate a random 3 letter word
def generate_word():
    word = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
    return word

#check if the word is in the dictionary
def check_is_word(word, file):
    try:
        with open(file, 'r') as file:
            contents = file.read()
            words = contents.split()
            if word in words:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"File '{file}' not found.") 

def select_word():
    valid = False
    while valid == False:
        word = generate_word()
        valid = check_is_word(word, WORD_FILE)
    print(word)
    return word
    

## main part of code ##
goal = select_word()           
print(f"the word to guess is {goal}")

guess = input("enter a 3 letter word: ")
if check_is_word(guess,WORD_FILE):
    if guess == goal:
        print("congrats you guessed the word!")
    else:
        print("sorry that is not correct :/")
else:
    input("Not a valid word")
