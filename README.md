# ✂️ Rock Paper Scissors — CLI Game

A fun terminal-based **Rock Paper Scissors** game built in Python. Play as many rounds as you want against the computer and see who comes out on top!

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Libraries](https://img.shields.io/badge/library-random%20%28stdlib%29-lightgrey)

---

## 🎮 Gameplay Preview

```
How many times you want to play? : 3

Enter Your Choice : R
You Won!  Python chose P and You chose R
--------------------Next Round----------------

Enter Your Choice : S
Tie!  Python chose S and You chose S
--------------------Next Round----------------

Enter Your Choice : P
Python Won!  Python chose S and You chose P

-----------------------------------------
Congratulations You Won!
Your Score  : 2
Python Score: 1
Times Drawn : 1
```

---

## 🕹️ How to Play

1. Run the script
2. Enter how many rounds you want to play
3. Each round, type your choice:
   - `R` — Rock
   - `P` — Paper
   - `S` — Scissors
4. The computer picks randomly — whoever wins the most rounds wins the game!

### Win Conditions
| You chose | Computer chose | Result |
|-----------|---------------|--------|
| Paper | Rock | ✅ You Win |
| Scissors | Paper | ✅ You Win |
| Rock | Scissors | ✅ You Win |
| Same | Same | 🤝 Draw |
| Anything else | — | ❌ Python Wins |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- No external libraries — uses only the built-in `random` module

### Run the Game

```bash
python rps.py
```

---

## 🧠 How It Works

- `random.choice(['R', 'P', 'S'])` picks the computer's move each round
- Your input is converted to uppercase so `r`, `p`, `s` all work too
- Scores are tracked across all rounds with `user_score`, `py_score`, and `draw` counters
- At the end, the final scoreboard and winner are displayed

---

## 🗺️ Roadmap

- [x] Multi-round gameplay
- [x] Score tracking (wins, losses, draws)
- [x] Case-insensitive input
- [ ] Input validation (handle invalid choices like `X` or `123`)
- [ ] Best-of-N mode (e.g. first to 3 wins)
- [ ] Leaderboard / high score saving
- [ ] GUI version (Tkinter)

---

## 👤 Author

**Ez-Saksham**  
GitHub: [@Ez-Saksham](https://github.com/Ez-Saksham)

---

> Made with 🐍 Python as a fun learning project. Give it a ⭐ if you enjoyed it!
