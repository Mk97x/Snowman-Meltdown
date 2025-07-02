import random

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # TODO: Build your game loop here.
    # For now, simply prompt the user once:
    print(STAGES[mistakes])
    underlines = ["_"] * len(secret_word)
    print(" ".join(underlines))
    print()
    while mistakes < 3:
        guess = input("Guess a letter: ").lower()
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            print("You guessed:", guess)
        else: 
            print("You already guessed that letter - focus")

        if guess in secret_word:
            index = secret_word.find(guess)
            print("That letter is correct")
            print(STAGES[mistakes])
            underlines[index] = guess
            print(" ".join(underlines))
            
        else:
            print("That letter is not appear to be in the word")
            mistakes += 1
            print(STAGES[mistakes])
            print(" ".join(underlines))
        
    
if __name__ == "__main__":
    play_game()