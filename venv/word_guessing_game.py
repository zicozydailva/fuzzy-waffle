import random
import re

def read_words():
    try:
        with open('words.txt', 'r') as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print("words.txt file not found. Please ensure the file exists.")
        return []
    
    
def display_word(secret_word, guessed_letters):
    word_to_display = ''
    
    for letter in secret_word:
        if letter in guessed_letters:
            word_to_display += letter
        else:
            word_to_display += '_ '
            
    print("Word: ", word_to_display.strip())
   
def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif not re.search("^[a-z]$", guess):
            print("Invalid input! Please enter a lowercase letter.")
        elif guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            return guess
        
def is_word_guessed(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

def main():
    words = read_words()
    if not words:
        return
    
    secret_word = random.choice(words)
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to the Word Guessing Game!")
    
    while attempts > 0:
        display_word(secret_word, guessed_letters)
        print(f"Attempts remaining: {attempts}")
        
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)
        
        if guess not in secret_word:
            attempts -= 1
            print(f"Wrong guess! The letter '{guess}' is not in the word.")
        
        if is_word_guessed(secret_word, guessed_letters):
            print(f"Congratulations! You've guessed the word: {secret_word}")
            break
    else:
        print(f"Sorry, you've run out of attempts. The word was: {secret_word}")