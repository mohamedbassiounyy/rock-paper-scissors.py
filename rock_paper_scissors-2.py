# start the game
# ask the player to make a move (r, p, s)
# pc would select a move randomly
# check player won or lose or tie
# pc == player --> tie
# player == 'r' and pc == 's' or player == 'p' and pc == 'r' or player == 's' and pc == 'p'
# you won!
# any other case
# you lose! pc won
import random
# rock paper scissors
CHOICES = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

def get_player_choice():
    """Prompt the player for a valid choice and return it."""
    while True:
        choice = input("What's your choice? (r -> Rock || p -> Paper || s -> Scissors)\n").lower().strip()
        # Check for valid choices including variations
        if choice in ['rock', 'r', 'ROCK', 'Rock' ]:
            return 'r'
        elif choice in ['scissors', 's', 'SCISSORS', 'Scissors']:
            return 's'
        elif choice in ['paper', 'p' , 'PAPER', 'Paper']:
            return 'p'
        else:
            print("Invalid choice. Please select 'r', 'p' or 's'")
def play_round():
    """Play a single round of rock-paper-scissors."""
    player = get_player_choice()
    pc = random.choice(list(CHOICES.keys()))
    
   
    print(f"Player: {CHOICES[player]}\nPC: {CHOICES[pc]}")
    print(f"Player: {CHOICES[player]} vs PC: {CHOICES[pc]}")
    
    if player == pc:
        print("It's a tie!")
        return 'tie'
    elif (player == 'r' and pc == 's') or (player == 'p' and pc == 'r') or (player == 's' and pc == 'p'):
        print("You won!")
        return 'player'
    else:
        print("You lose! PC won")
        return 'pc'

def play_game():
    """Main game loop to play multiple rounds."""
    player_score, pc_score = 0, 0
    
    while True:
        result = play_round()
        
        if result == 'player':
            player_score += 1
        elif result == 'pc':
            pc_score += 1
        
        print(f"Score - Player: {player_score} | PC: {pc_score}")
        
        if input("Play again? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    play_game()
