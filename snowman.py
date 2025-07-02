import random
import ascii_art as art


WORDS = ["python", "git", "github", "snowman", "meltdown"]
STAGES = art.STAGES

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current game state"""
    print(STAGES[mistakes])
    
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("Word:", display_word)
    print()

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line
    

    display_game_state(mistakes, secret_word, guessed_letters)
    
    while mistakes < 3:
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess.strip()) > 1:
                print("Only single letter inputs are allowed")
                continue
            elif len(guess.strip()) == 1:
                break
        
  
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            print("You guessed:", guess)
        else: 
            mistakes +=1
            print("You already guessed that letter - focus")
            continue  


        if guess in secret_word:
            print("That letter is correct")
        else:
            print("That letter does not appear to be in the word")
            mistakes += 1
        

        display_game_state(mistakes, secret_word, guessed_letters)
        

        if all(letter in guessed_letters for letter in secret_word):
            print(f"You correctly guessed the word {secret_word}")
            break
        

        if mistakes >= 3:
            print("Game Over! The snowman melted completely!")
            print(f"The word was: {secret_word}")
            False
        

if __name__ == "__main__":
    play_game()