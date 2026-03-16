# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The game's purpose is to provide an interactive number guessing game built with Streamlit, where users select a difficulty level, guess a secret number within a range, receive hints, and accumulate scores based on performance, with a limited number of attempts.
- Bugs found: 1) Inconsistent score updates for "Too High" guesses that sometimes increased score; 2) Incorrect attempt counting that allowed fewer guesses than intended; 3) Invalid inputs consuming attempts unnecessarily.
- Fixes applied: Refactored core game logic functions (get_range_for_difficulty, parse_guess, check_guess, update_score) into logic_utils.py for better separation of concerns. Fixed scoring to deduct 5 points consistently for wrong guesses. Adjusted attempt initialization to 0 and increment only on valid guesses. Corrected win points calculation to properly reflect attempt number.

## 📸 Demo

- Screenshot of the fixed game running successfully, showing a winning scenario with correct hints and scoring.

## 🚀 Stretch Features

- Completed Challenge 1: Advanced Edge-Case Testing. Added a pytest test case for score updates on wrong guesses, and verified all tests pass. Screenshot of pytest results showing 4 passed tests.
