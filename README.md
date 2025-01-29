# Dogdle 🐶
#### Video Demo: <https://youtu.be/W_Lk8Xn-dA0>

#### Description: 
Dogdle is a command-line guessing game inspired by Wordle, where the player has to guess the name of a dog within six attempts. Instead of regular words, Dogdle challenges you to identify a 5-letter dog name, making it a perfect game for dog lovers and word puzzle enthusiasts!

#### Features:
* Themed Feedback: The game uses the rich library to provide colored feedback based on your guesses:
* Randomized Dog Names: The game randomly selects a 5-letter dog name from a list, ensuring that every game is different.

#### How to play:
1. Start the Game: Run the script in your terminal.
2. Guess the Dog Name: Type in a 5-letter guess for the dog's name.
3. Get Feedback: The game will provide visual feedback on your guess:
   - Green letters are correct and in the correct position.
   - Orange letters are correct but in the wrong position.
   - Grey letters are incorrect.
4. Win or Lose: If you guess the name correctly within six attempts, you win! If not, the correct answer will be revealed.

#### If you'd like to try it out:
1.  Download the **dog_names.txt** file (or make your own list) in the same folder as **dogdle.py**.
2.  Install rich library
```
pip install rich
```
3.  Run the program
```
python dogdle.py
```
 
