# Programming Challenge: Escape the Loop!

## Overview
You are trapped in a maze with **10 energy points**. Each turn, you must choose an action. Random events happen that affect your energy. Can you escape before running out of energy?

This challenge combines several Python concepts you have been learning:
- Variables
- Loops (`while`)
- Conditionals (`if`, `elif`, `else`)
- User input
- Sequences (optional)
- The `random` module

---

## Game Rules

### Starting Conditions
- Player begins with **10 energy points**.
- The game continues as long as **energy > 0** and ends when:
  - Energy reaches **20** → Player escapes and wins
  - Energy drops to **0** → Player loses

---

### Actions Per Turn
1. **Move**
   - Try to move through the maze.
   - Random outcomes:
     - 50% chance: lose 2 energy
     - 30% chance: nothing happens
     - 20% chance: find food, gain 3 energy

2. **Rest**
   - Stay in place and regain **2 energy**.
   - Always succeeds but wastes a turn.

3. **Guess**
   - Program generates a random number between 1 and 5.
   - Player guesses the number:
     - Correct guess → gain 5 energy
     - Wrong guess → lose 2 energy

4. **Invalid input**
   - If the player enters an invalid action, they lose 1 energy.

---

## Advanced Version (Additional Complexity)

For groups who want a more challenging version:

1. **Track position using complex numbers**
   - Player starts at `0 + 0j`.
   - Move action updates position:
     - East: `+1 + 0j`
     - North: `0 + 1j`
     - West: `-1 + 0j`

2. **Keep a history of turns**
   - Track action, energy, and position for each turn.
   - Display the summary at the end.

3. **Random event probabilities remain the same**
   - Move: stumble (lose 2), nothing (0), find food (gain 3)
   - Rest: gain 2
   - Guess: correct (gain 5), incorrect (lose 2)

4. **Optional Extensions**
   - Add monsters or traps as random events.
   - Track number of turns to escape.
   - Store all energy changes in a list and print a simple “graph” of progress.
   - Add more complex puzzles for the guess action (e.g., math challenges or multi-digit random numbers).

---

## Suggested Python Concepts
- Variables to track energy, turn count, position
- `while` loop to control the game flow
- `if / elif / else` statements to handle actions and events
- `input()` to capture player decisions
- `random` module for unpredictable events
- Lists (optional) to track history

---

## Goal
- Reach **20 energy** to escape the maze.
- Avoid dropping to **0 energy**.
- Have fun experimenting with randomness, loops, and conditionals!

---

**Tip for Students:**  
Start with the baseline version if unsure, then try the advanced version for a more complex and fun challenge!
