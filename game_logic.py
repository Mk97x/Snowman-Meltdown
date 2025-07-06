import random
import ascii_art as art


WORDS = ["python", "git", "github", "snowman", "meltdown"]
STAGES = art.STAGES
ALPHABET = "abcdefghijklmnopqrstuvwxyz" # english alphabet to check input is in fact a letter 

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)] # choose random word from WQRDS

def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current game state"""
    print(STAGES[mistakes])

    
    display_word = "" # empty str to build the underlines-gui
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " " # if letter in word, add letter and space
        else:
            display_word += "_ " # else add underline+space
    
    print("Word:", display_word)
    print()

def ask_to_replay():
    play_again = input("Do you wanna play again? (y/n) ").lower().strip()
    while True:
        try:
            if play_again == "y" or play_again == "yes":
                play_game()
                return None
            else:
                break
        except TypeError:
            print("I need y or n as input.")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    print("Welcome to Snowman Meltdown!")
    # print("Secret word selected: " + secret_word)  
    
    display_game_state(mistakes, secret_word, guessed_letters)
    
    while mistakes < 3: # 3 lifes
        while True: # try input until it is valid
            guess = input("Guess a letter: ").lower().strip() # strip for potential whitespaces
            if len(guess) > 1 or guess not in ALPHABET:
                print("Only single letter inputs are allowed")
                continue
            elif len(guess) == 1:
                break
        
  
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            print("You guessed:", guess)
        else: 
            mistakes +=1
            print("You already guessed that letter - focus")
            print(STAGES[mistakes])
            continue  


        if guess in secret_word:
            print("That letter is correct")
        else:
            print("That letter does not appear to be in the word")
            mistakes += 1
        

        display_game_state(mistakes, secret_word, guessed_letters)
        

        if all(letter in guessed_letters for letter in secret_word): # check if all letters from secret word are guessed
            print(f"You correctly guessed the word {secret_word}")
            break
        

        if mistakes >= 3: # losing screen after 3 wrong tries
            print("Game Over! The snowman melted completely!")
            print(f"The word was: {secret_word}")
            False

    ask_to_replay()

        

if __name__ == "__main__":
    play_game()