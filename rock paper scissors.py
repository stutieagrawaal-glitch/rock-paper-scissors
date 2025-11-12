#rock paper scissors game


import random
while True:
    options = ['rock','scissors','paper']
    object = random.choice(options)
    player_score = 0
    computer_score = 0
    counter = input("choose from rock,paper or scissors: ").lower()
    if object == "rock" and counter == "paper" :
        print("you won!!")
        print("i chose: ", object)
        player_score += 1
        print(player_score)
    elif object == "rock" and counter == "rock":
        print("its a tie!")
        print("i chose: ", object)
    elif object == "scissors" and counter == "rock":
        print("you won!!")
        print("i chose: ", object)
        player_score += 1
        print(player_score)
    elif object == "scissors" and counter == "scissors":
        print("its a tie!")
        print("i chose: ", object)
    elif object == "paper" and counter == "rock":
        print("you won!!")
        print("i chose: ", object)
        player_score += 1
        print(player_score)
    elif object == "paper" and counter == "paper":
        print("its a tie!")
        print("i chose: ", object)
    else:
        print("you lost!")
        print("i chose: ", object)
        computer_score += 1
        print(computer_score)
