import random

class Game:
    def __init__(self):
        self.user_name = "User"
        self.pc_name = "Computer"
        self.user_choice = None
        self.comp_choice = None

    def get_user_choice(self):
        print("Welcome to Rock Paper Scissors Game!")
        self.user_choice = input("Enter r (rock), p (paper), or s (scissors): ").lower()
        if self.user_choice not in ['r', 'p', 's']:
            raise ValueError("Invalid input! Please enter only 'r', 'p', or 's'.")
        return self.user_choice

    def get_computer_choice(self):
        choice = random.choice(['r', 'p', 's'])
        self.comp_choice = choice
        return self.comp_choice

    def determine_winner(self):
        if self.user_choice == self.comp_choice:
            return "It's a tie!"
        elif (self.user_choice == 'r' and self.comp_choice == 's') or \
             (self.user_choice == 'p' and self.comp_choice == 'r') or \
             (self.user_choice == 's' and self.comp_choice == 'p'):
            return f"{self.user_name} wins!"
        else:
            return f"{self.pc_name} wins!"





                
        