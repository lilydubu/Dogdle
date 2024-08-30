from rich.console import Console
from rich.theme import Theme
import random

dogdle = Theme({
    "correct": "bold on spring_green1",
    "misplaced" : "bold on sandy_brown",
    "wrong" : "bold on grey37",
    "win" : "bold spring_green1",
    "lose" : "bold indian_red1",
    "dog" : "bold"
})

console = Console(width= 40, theme=dogdle, style="dog")

# Randomizer for names
def generate():
    f = open("dog_names.txt").read().splitlines()
    return random.choice(f).upper()

# Clear the console
def refresh():
    console.clear()
    console.rule(f":dog: DOGDLE :dog:")
    
# Validate input
def check_input(index):
    while(True):
        guess = input(f"Guess {index+1}: ").upper()
        if guess.isalpha() and len(guess) == 5: 
            return guess
        else:
            print("Invalid input.")

# Display the game progress
def update_progress(secret, guesses):
    for guess in guesses:
        styled = []
        for letter, correct in zip(guess, secret):
            if letter == correct:
                style = "correct"
            elif letter in secret:
                style = "misplaced"
            else:
                style = "wrong"
            styled.append(f"[{style}]{letter}[/]")
        console.print("".join(styled), justify="center")
    

def main():
    secret = generate()
    guesses = [["_"] * 5] * 6
    won = False
    
    for i in range(7):
        refresh()
        update_progress(secret, guesses)
        
        if won:
            console.print("You won!", style="win")
            return 0

        else:
            if i < 6:
                guesses[i] = check_input(i)
                if guesses[i] == secret:
                    won = True
            else:
                console.print(f"You lose! The answer was {secret}", style="lose")
                return 0

main()
