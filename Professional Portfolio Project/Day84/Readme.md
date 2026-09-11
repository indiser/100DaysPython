# Day 84: Tic Tac Toe AI

## 📌 Project Overview
A terminal-based Tic Tac Toe game where the player (X) faces an unbeatable AI (O) powered by the Minimax algorithm with alpha-beta pruning.

## 🚀 Features
- **Unbeatable AI** - Minimax algorithm guarantees AI never loses
- **Alpha-Beta Pruning** - Optimizes search by cutting off irrelevant branches
- **Move Ordering** - Center and corners evaluated first for faster pruning
- **Colored Output** - X in red, O in blue, board in bold (ANSI escape codes)
- **Input Validation** - Handles non-numeric input and occupied cell attempts

## 🧠 How the AI Works
- AI plays as `O`, human plays as `X`
- `minimax()` recursively simulates all possible game states
- Scores: AI win = `10 - depth`, Human win = `depth - 10`, Draw = `0`
- Depth penalty ensures AI prefers faster wins
- `get_best_move()` picks the highest-scoring available move

## ▶️ Usage
```bash
python tic-tac-toe.py
```
Enter a number 1–9 to place your move (positions map left-to-right, top-to-bottom).

## 📁 Files
| File | Description |
|------|-------------|
| `tic-tac-toe.py` | Complete game — Board class, Minimax AI, game loop |
