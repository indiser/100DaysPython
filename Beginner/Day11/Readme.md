# Blackjack Game

A command-line Blackjack game implemented in Python.

## Features

- Classic Blackjack gameplay (Hit/Stand)
- Automatic Ace conversion (11→1 when busting)
- Dealer AI (draws until 17+)
- Win/Loss/Push detection
- ASCII art logo

## How to Play

1. Run `BlackJack.py`
2. Choose "Hit" to draw a card or "Stand" to end your turn
3. Get closer to 21 than the dealer without going over
4. Dealer reveals hidden card when you stand

## Files

- `BlackJack.py` - Main game logic
- `blacjack_art.py` - ASCII art logo

## Rules

- Dealer must draw until reaching 17 or higher
- Aces count as 11 or 1 (automatically adjusted)
- Face cards (J, Q, K) count as 10
- Blackjack = exactly 21
