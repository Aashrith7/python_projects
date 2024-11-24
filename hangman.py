from random_word import RandomWords

# Initialize the RandomWords class
r = RandomWords()

# Get a random word and convert it to lowercase
chosen_word = r.get_random_word().lower()
word_display = ['_' for _ in chosen_word]
attempts = 8

print("Welcome to Hangman!") 

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("The letter doesn't appear in the word.")
        attempts -= 1
        print(f"Attempts remaining: {attempts}")

if '_' not in word_display:
    print("\nCongratulations! You guessed the word!")
    print(' '.join(word_display))
else:
    print(f"\nYou ran out of attempts. The answer was: {chosen_word}")
    print("You lost.")
