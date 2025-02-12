# Jogo da Velha em Python 🎮

Um jogo da velha interativo implementado em Python com suporte para dois modos de jogo: jogador contra jogador (PvP) ou jogador contra computador (PvC).

## 📋 Características

- Interface de linha de comando limpa e intuitiva
- Dois modos de jogo:
  - Jogador contra Jogador
  - Jogador contra Computador
- Tabuleiro numerado para fácil referência das posições
- Compatível com Windows e sistemas Unix-like
- Sistema de jogadas alternadas
- Verificação automática de vitória/empate
- Opção de jogar novamente ao final de cada partida

## 🚀 Como Executar

1. Certifique-se de ter Python instalado em seu sistema
2. Baixe o arquivo do jogo
3. Abra o terminal na pasta do arquivo
4. Execute o comando:
```bash
python jogo_da_velha.py
```

## 🎯 Como Jogar

1. Ao iniciar, escolha o modo de jogo:
   - Digite 's' para jogar contra o computador
   - Digite qualquer outra tecla para jogar contra outro jogador

2. Se escolher jogar contra o computador:
   - Escolha seu símbolo ('X' ou 'O')
   - O computador usará o símbolo oposto

3. O tabuleiro usa números de 1 a 9 para representar as posições:
```
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
```

4. Em seu turno, digite o número da posição desejada (1-9)

5. O jogo continua até que:
   - Um jogador vença (três símbolos iguais em linha)
   - Ocorra um empate (todas as posições preenchidas)

6. Ao final, você pode escolher jogar novamente

## 🛠️ Requisitos do Sistema

- Python 3.x
- Sistema operacional: Windows, Linux, ou macOS

## 🤝 Contribuindo

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias para o jogo. Algumas ideias de melhorias:

- Adicionar um modo de dificuldade para o computador
- Implementar uma interface gráfica
- Adicionar sistema de pontuação
- Incluir sons e efeitos visuais
- Criar um modo online para jogar pela rede

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir como desejar.