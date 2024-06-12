import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    user_choice = input("Enter your choice (rock , r , paper , p , or scissors , s): ").lower()
    while user_choice not in ['rock','r' , 'paper','p' , 'scissors','s']:
        print("Invalid choice. Please choose again.")
        user_choice = input("Enter your choice (rock , r , paper , p , or scissors , s): ").lower()
    return user_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock','r' and computer_choice == 'scissors') or \
         (user_choice == 'paper','p' and computer_choice == 'rock') or \
         (user_choice == 'scissors','s' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("\nDo you want to play again? (yes or no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
