from random import randint

computador = randint(1,5)

jogador = int(input('Digite um número de 1 a 5 » '))

if computador == jogador:
    print(f'Acertou!\
          \nComputador » {computador}\
          \nJogador » {jogador}')
else:
     print(f'Errou!\
          \nComputador » {computador}\
          \nJogador » {jogador}')