import random
moves = 'R for rock, P for paper,S for scissors'
print(f'The possible moves are: {moves}')
pmoves = ["R", "P", "S"]

continue_playing = True

while continue_playing == True:
    cpu = random.choice(pmoves).upper()
    player = input("what's your move? R, P or S? ").upper()
    print(f"The Cpu's choose is {cpu}")
    if cpu == player:
        print("Tie")
    
    elif player == 'P' and cpu == 'R':
        print('Player wins')

    elif cpu == 'R' and player == 'S':
        print('CPU wins')

    elif player == 'R' and cpu == 'S':
        print('Player wins')
    
    elif cpu == 'P' and player == 'R':
        print('CPU wins')

    elif player == 'S' and cpu == 'P':
        print('Player wins')

    elif cpu == 'S' and player == 'P':
        print('CPU wins')
    else:
        print("Invalid User Input")
    end_game = input('Do you wish to continue ths game? y for YES and n for NO ')
    if end_game.lower() == 'y':
        continue
    elif end_game.lower() == 'n':
        continue_playing = False
