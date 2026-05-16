# Python-project
Here I will upload all my python projects that I have build during my course

# 🃏 War Card Game (Python Simulation)

A simple Python simulation of the classic **War card game** between two players.  
This project focuses on object-oriented programming, game logic design, and state management in Python.

---

## 📌 Features

- Fully automated 2-player card game
- Implements classic **War rules**
- Handles recursive “war” situations
- Detects early game termination when a player cannot continue
- Round-by-round game simulation with console output

---

## 🧠 Game Rules

1. A standard deck (values 2–14) is shuffled and split equally between two players.
2. Each round:
   - Both players draw one card.
   - Higher card wins the round.
   - Winner collects both cards and adds them to their deck.
3. If both cards are equal:
   - A **War** begins:
     - Each player places 3 cards face-down
     - Then draws another card for comparison
     - Winner takes all cards in the pile
4. If a player does not have enough cards during war, they lose the game.

---

## 🏗️ Tech Concepts Used

- Python OOP (Classes, Methods, Classmethod, Staticmethod)
- List operations (queue simulation using `pop(0)`)
- Game loop design
- Conditional logic and recursion-like war handling
- State management between rounds

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/utkarshsingh003/war-card-game.git
