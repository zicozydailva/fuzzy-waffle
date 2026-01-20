import random

def generate_secret():
    digits = list(range(10))
    random.shuffle(digits)
    return '.join(str(digit) for digit in digits[:4])'

def calculate_cows_and_bulls(secret, guess):
    bulls = sum([1 for i in range(4) if guess[i] == secret[i]])
    cows = sum([1 for digit in guess if digit in secret]) - bulls
    return cows, bulls

def main():
    secret = generate_secret()
    print('I have generated a 4-digit number with unique digits. Try to guess it!')
    
    while True:
        guess = input('Enter your 4-digit guess: ').strip()
        
        if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
            cows, bulls = calculate_cows_and_bulls(secret, guess)
            print(f'Cows: {cows}, Bulls: {bulls}')
            
            if bulls == 4:
                print('Congratulations! You guessed the number correctly!')
                break
        else:
            print('Invalid input! Please enter a 4-digit number with unique digits.')       

main()