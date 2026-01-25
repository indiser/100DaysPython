import os
import time

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


class Board:
    def __init__(self):
        self.slots=[" "]*9
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display(self):
        self.clear_screen()
        
        print(f"{Colors.HEADER}{Colors.BOLD}   TIC - TAC - TOE   {Colors.RESET}\n")
        
        formatted_slots = []
        for slot in self.slots:
            if slot == "X":
                formatted_slots.append(f"{Colors.RED} X {Colors.RESET}")
            elif slot == "O":
                formatted_slots.append(f"{Colors.BLUE} O {Colors.RESET}")
            else:
                formatted_slots.append("   ")
        
        # The Grid Construction
        print(f" {formatted_slots[0]} | {formatted_slots[1]} | {formatted_slots[2]} ")
        print(f"{Colors.BOLD}-----+-----+-----{Colors.RESET}")
        print(f" {formatted_slots[3]} | {formatted_slots[4]} | {formatted_slots[5]} ")
        print(f"{Colors.BOLD}-----+-----+-----{Colors.RESET}")
        print(f" {formatted_slots[6]} | {formatted_slots[7]} | {formatted_slots[8]} ")
        print("\n")

    def update_board(self, position, player):
        index=position-1
        
        self.slots[index]=player
    
    def check_winner(self):
        winning_combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # Cols
            (0, 4, 8), (2, 4, 6)             # Diagonals
        ]
        
        for a, b, c in winning_combos:
            if(self.slots[a]==self.slots[b]==self.slots[c]) and self.slots[a] != " ":
                return self.slots[a]
            
        return None
    
    def minimax(self, is_maximizing):
        # 1. Base Case: Check if the game is over
        winner = self.check_winner()
        if winner == "O": # AI wins (assuming AI is 'O')
            return 1
        if winner == "X": # Human wins
            return -1
        if " " not in self.slots: # Draw
            return 0
            
        # 2. Recursive Step
        if is_maximizing: # AI's Turn (Try to get highest score)
            best_score = -float('inf')
            for index in range(9):
                if self.slots[index] == " ":
                    self.slots[index] = "O" # Make the move
                    score = self.minimax(False) # Call self (Recursion!)
                    self.slots[index] = " " # Undo the move (Backtrack)
                    best_score = max(score, best_score)
            return best_score
            
        else: # Human's Turn (Try to get lowest score for AI)
            best_score = float('inf')
            for index in range(9):
                if self.slots[index] == " ":
                    self.slots[index] = "X" # Make move
                    score = self.minimax(True) # Call self
                    self.slots[index] = " " # Undo move
                    best_score = min(score, best_score)
            return best_score
    
    def get_best_move(self):
        best_score = -float('inf')
        move = 0
        
        # Loop through all empty spots
        for index in range(9):
            if self.slots[index] == " ":
                self.slots[index] = "O" # AI tries this spot
                score = self.minimax(False) # Check outcome
                self.slots[index] = " " # Reset
                
                # If this is the best outcome so far, save it
                if score > best_score:
                    best_score = score
                    move = index
                    
        return move + 1 # Convert back to 1-9 for your update function
    


game = Board()

current_player = "X"

# The Game Loop
game_on = True
while game_on:
    # 1. Show the board
    game.display()
    
    if current_player == "X":
        prompt = f"Player {Colors.RED}X{Colors.RESET}, choose (1-9): "
        try:
            choice = int(input(prompt))
        except ValueError:
            print(f"{Colors.RED}Invalid input! Numbers only.{Colors.RESET}")
            time.sleep(1)
            continue
    else:
        # AI Turn
        print("AI is thinking...")
        choice = game.get_best_move()
    
    game.update_board(choice,current_player)
    
    if game.check_winner():
        game.display()
        print(f"Player {current_player} wins!")
        game_on = False
        

    if " " not in game.slots:
        game.display()
        print("It's a Draw!")
        game_on = False
    
    if current_player=='X':
        current_player='O'
    else:
        current_player='X'