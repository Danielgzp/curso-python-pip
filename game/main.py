import random

def choose_options():
    options = ('piedra', 'tijera', 'papel')
    user_option = input("Ingrese la opcion que desea jugar piedra/papel/tijera: ").lower()    
    computer_option = random.choice(options)    
    print("\nHas elegido la opcion: ", user_option)
    print("La opcion de la maquina es: ", computer_option)

    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if (user_option == computer_option):
        print('Han elegido la misma opcion, por lo cual es un empate!\n')
    elif(user_option == "tijera"):
        if(computer_option == "piedra"):
            print("La maquina eligio piedra, por lo cual has perdido")
            computer_wins += 1
        else:
            print("Felicidades has ganado!!!")
            user_wins += 1
    elif(user_option == "piedra"):
        if(computer_option == "papel"):
            print("La maquina eligio papel, por lo cual has perdido")
            computer_wins += 1
        else:
            print("Felicidades has ganado!!!")
            user_wins += 1
    elif(user_option == "papel"):
        if(computer_option == "tijera"):
            print("La maquina eligio tijera, por lo cual has perdido")
            computer_wins += 1
        else:
            print("Felicidades has ganado!!!")
            user_wins += 1
    
    return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
    print(f'''
    🤖 Computer wins: {computer_wins}
    🙋 User wins: {user_wins}
            ''')
    
    if (user_wins == 3):
        print('🎖️ El ganador es el Usuario 🎖️')
        print('\n**' * 2 + 'HA FINALIZADO EL JUEGO'+ '**\n' * 2)
        exit()
        
    if (computer_wins) == 3:
        print('🎖️ El ganador es la Computadora 🎖️')
        print('\n**** HA FINALIZADO EL JUEGO'+ '****\n')
        exit()


def run_game():
    rounds = 0
    user_wins = 0
    computer_wins = 0
    print('***' * 10)
    print("BIENVENIDO AL JUEGO DE PIEDRA, PAPEL Y TIJERA")
    print('***' * 10)

    while(True):
        rounds += 1
        print("\nRound ->", rounds)
        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        check_winner(user_wins, computer_wins)
       

run_game()

