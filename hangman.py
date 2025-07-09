import random

def hangman_game():
    words = ["coding", "hangman" ]
    
    word_to_guess = random.choice(words).lower()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    word_display = ["_" for _ in word_to_guess]
    
    print("Welcome to Hangman!")
    print("You have 6 incorrect guesses allowed.")
    print("Word to guess:", " ".join(word_display))
    
    while incorrect_guesses < max_incorrect_guesses:
        if "_" not in word_display:
            print(f"\nCongratulations! You won! The word was: {word_to_guess}")
            break
        
        print(f"\nIncorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")
        
        guess = input("Enter a letter: ").lower()
        

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
            
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    word_display[i] = guess
            
            print("Word:", " ".join(word_display))
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1
            
            # Simple hangman drawing
            hangman_stages = [
                "  +---+\n      |\n      |\n      |\n      |\n      |\n=========",
                "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
                "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
                "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
                "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
                "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
                "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
                "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
            ]
            
            if incorrect_guesses <= len(hangman_stages):
                print(hangman_stages[incorrect_guesses])
    
    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nGame Over! You've run out of guesses.")
        print(f"The word was: {word_to_guess}")
    
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again == 'y' or play_again == 'yes':
        hangman_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    hangman_game()