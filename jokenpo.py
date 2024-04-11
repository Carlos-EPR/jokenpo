from random import sample, randint

options = ["Pedra", "Papel", "Tesoura"]

def user_screen(opt):
    for index, op in enumerate(opt):
        print(f"{index + 1} = {op}")

    user_choice = int(input('Faça sua escolha! '))
    return opt[user_choice-1]

def computer_choice(content):
    sample(content, k=len(content))
    computer_chose = content[randint(0, 2)]
    return computer_chose

def check_result(player, computer):
    if player == computer:
        return 'Empate'
    elif (((player == "Pedra") and (computer == "Tesoura")) or
          ((player == "Papel") and (computer == "Pedra")) or
          ((player == "Tesoura") and (computer == "Papel"))):
        return "Você Ganhou!"
    return "Você Perdeu"

def play():
    print('''
    ---------------------------------
    Bem-vinda ao Pedra, Papel ou Tesoura.
    Escolha sua arma!.
    ''')

    player_result = user_screen(options)
    computer_result = computer_choice(options)

    print(f'Sua escolha: {player_result}')
    print(f' Adversario: {computer_result}')

    results = check_result(player_result, computer_result)
    print(f"\n{results}")

def main():
    play_again = ''
    while play_again.lower() != 'n':
        play()
        print(f'Jogar novamente? ')
        play_again = input('Digite \'s\' para sim ou \'n\' para não: ')

main()