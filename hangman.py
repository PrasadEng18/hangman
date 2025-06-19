import random

def main():
    word_list = ["python", "hangman", "computer", "programming", "keyboard"]
    secret_word = random.choice(word_list).lower()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6
    current_display = ["_"] * len(secret_word)
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_attempts and "_" in current_display:
        print("\n" + " ".join(current_display))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print("Correct!")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    current_display[i] = guess
        else:
            print("Incorrect!")
            incorrect_guesses += 1
    
    if "_" not in current_display:
        print(f"\nCongratulations! You guessed the word: {secret_word}")
    else:
        print(f"\nGame over! The word was: {secret_word}")

if __name__ == "__main__":
    main()