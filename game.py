import random
while True:
    user_input = input("enter your choice(rock,paper,scissor)  ")
    action = ["rock","paper","scissor"]
    computer_input = random.choice(action)
    print(f"\n you choose {user_input}, computer choose {computer_input}.\n")

    if user_input == computer_input:
        print(f"both player select{user_input}. it's tie")
    elif user_input == "rock":
        if computer_input == "scissor":
            print("rock smash scissor ! you win!")
        else:
            print("paper cover rock ! you lose1")
    elif user_input == "paper":
        if computer_input == "rock":
            print("paper cover rock you win!")
        else:
            print("scissor cut paper ! you lose!")

    elif user_input ==  "scissor":
        if computer_input == "paper":
            print("scissor cut paper! you win!")
        else:
            print("rock smash scissor! you lose")
    else:
        print("invalid input ,give correct input ")

    play_again = input("play again (y/n): ").lower()
    if play_again != "y":
        print("thank for playing ")
        break



