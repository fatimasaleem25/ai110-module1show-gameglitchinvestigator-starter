# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- The game is a number guessing game built with Streamlit, where players guess a secret number within a range based on difficulty, with limited attempts and scoring.
- Bug 1: Inconsistent score updates - when the guess is "Too High", the score sometimes increases by 5 points and sometimes decreases by 5 points depending on the attempt number being even or odd, which is confusing and not logical.
- Bug 2: Incorrect attempt counting - the game allows fewer guesses than intended; for example, on Normal difficulty with 7 attempts allowed, it only lets you make 6 guesses before declaring game over.
- Bug 3: Invalid inputs count as attempts - entering non-numeric input like letters still consumes an attempt and adds the invalid text to the guess history, which shouldn't happen.

---

## 2. How did you use AI as a teammate?

- I used GitHub Copilot in VS Code for code refactoring, bug fixing, and test generation.
- Correct suggestion: Copilot's Agent mode correctly suggested moving the game logic functions from app.py to logic_utils.py and updating the imports, which improved code organization without breaking functionality.
- Incorrect/misleading suggestion: When initially analyzing the scoring bug, Copilot suggested a complex conditional logic to "balance" the score changes, but I recognized it was unnecessary and simplified it to consistent deductions, which was more appropriate.

---

## 3. Debugging and testing your fixes

- I verified fixes by running the Streamlit app manually to check gameplay, ensuring hints were correct, scores updated properly, and attempts counted accurately. Additionally, I ran pytest to confirm automated tests passed.
- I wrote a new pytest test case (test_score_update_wrong_guess) that verifies score decreases by 5 points for both "Too High" and "Too Low" outcomes, which helped confirm the scoring fix. The test passed along with existing tests, showing the logic now works correctly.
- Copilot helped generate the test structure and assertions, but I specified the exact behavior to test based on the bug I fixed.

---

## 4. What did you learn about Streamlit and state?

- The secret number kept changing in the original app because Streamlit reruns the entire script on every user interaction (like button clicks), and without proper session state management, variables were reinitialized each time.
- Streamlit reruns happen whenever the user interacts with widgets; it's like the app restarts but preserves session_state variables across reruns. Session state is key to maintaining data like the secret number between interactions.
- I fixed it by ensuring the secret is set only once per game in session_state, and resetting it appropriately on new games or difficulty changes.

---

## 5. Looking ahead: your developer habits

- One habit I want to reuse is using automated tests (pytest) to verify fixes after changes, as it provides quick feedback and catches regressions.
- Next time, I would ask the AI for more specific, targeted fixes rather than broad suggestions, and always verify changes with both manual testing and automated tests before accepting them.
- This project changed my view on AI-generated code by showing that while AI can produce functional code quickly, it often contains subtle bugs that require careful human review and testing to ensure reliability and user experience.
