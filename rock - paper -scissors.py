import random 

def play_game() :
    options = ["rock","paper","scissors"]

    print("welcome to rock paper scissors game!")
    print("type rock,paper,or scissors")

    while True :
        user_choice = input("enter your choice : ").lower()
        computer_choice = random.choice(options)

        if user_choice not in options :
            print("invalid choice! try again")
            continue
        print("computer chose",computer_choice)

        if user_choice == computer_choice :
            print("it's a tie")
        
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper") :
            print("you win!")
        else :
            print("computer wins")

        play_again = input("do you a want to play again? (yes/no) :").lower()

        if play_again != "yes" :
            print("thanks for playing")
            break

play_game()

