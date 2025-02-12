import os
import random

def clear():
    """Limpa a tela de forma compatível com Windows e outros SOs."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(board):
    """Exibe o tabuleiro do jogo da velha de forma formatada."""
    print()
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print()

def check_winner(board):
    """
    Verifica se há um vencedor.
    Retorna 'X' ou 'O' caso haja vencedor; caso contrário, retorna None.
    """
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
        (0, 4, 8), (2, 4, 6)              # Diagonais
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c]:
            return board[a]
    return None

def get_available_moves(board):
    """Retorna os índices (0 a 8) das posições que ainda não foram marcadas."""
    return [i for i, spot in enumerate(board) if spot not in ['X', 'O']]

def switch_player(current):
    """Alterna o jogador: de 'X' para 'O' e vice-versa."""
    return 'O' if current == 'X' else 'X'

def main():
    # Verifica se o usuário deseja jogar contra o computador
    computer_mode = False
    mode = input('Deseja jogar contra o computador? ("s" para sim): ').lower().strip()
    if mode == 's':
        computer_mode = True

    # Se for contra o computador, permite escolher o símbolo do jogador
    if computer_mode:
        human_symbol = input('Escolha seu símbolo ("X" ou "O"): ').upper().strip()
        if human_symbol not in ['X', 'O']:
            print('Símbolo inválido. Você será "X" por padrão.')
            human_symbol = 'X'
        computer_symbol = 'O' if human_symbol == 'X' else 'X'
    else:
        human_symbol = None  # Não é necessário no modo dois jogadores
        computer_symbol = None

    play_again = True
    while play_again:
        # Inicializa o tabuleiro com números de 1 a 9 (strings) para indicar posições disponíveis
        board = [str(i) for i in range(1, 10)]
        current_player = 'X'  # O jogador 'X' sempre começa
        game_over = False

        while not game_over:
            clear()
            display_board(board)

            # Exibe a mensagem da vez
            if computer_mode:
                if current_player == human_symbol:
                    print("Sua vez. Você é '{}'.".format(human_symbol))
                else:
                    print("Vez do computador ({}).".format(computer_symbol))
            else:
                print("Jogador {}'s vez.".format(current_player))

            available_moves = get_available_moves(board)
            if current_player == computer_symbol and computer_mode:
                # Jogada do computador: escolhe aleatoriamente dentre as posições disponíveis
                move = random.choice(available_moves)
                print("O computador escolheu a posição {}.".format(board[move]))
            else:
                # Jogada do jogador (ou dos dois jogadores no modo 2 players)
                try:
                    move_input = input("Escolha uma posição (1-9): ").strip()
                    move = int(move_input) - 1  # Converte para índice 0-8
                    if move not in available_moves:
                        print("Posição inválida ou já ocupada. Pressione Enter para tentar novamente.")
                        input()
                        continue
                except ValueError:
                    print("Entrada inválida. Pressione Enter para tentar novamente.")
                    input()
                    continue

            # Registra a jogada
            board[move] = current_player

            # Verifica se houve vencedor ou empate
            winner = check_winner(board)
            if winner is not None:
                game_over = True
            elif not get_available_moves(board):
                game_over = True
                winner = None
            else:
                current_player = switch_player(current_player)

        clear()
        display_board(board)
        if winner is not None:
            if computer_mode:
                if winner == human_symbol:
                    print("Parabéns! Você venceu!")
                else:
                    print("O computador ganhou. Boa sorte na próxima!")
            else:
                print("Parabéns, jogador {}! Você venceu!".format(winner))
        else:
            print("O jogo terminou em empate.")

        again = input('Deseja jogar novamente? ("s" para sim): ').lower().strip()
        play_again = (again == 's')

    print("Obrigado por jogar!")

if __name__ == '__main__':
    main()
