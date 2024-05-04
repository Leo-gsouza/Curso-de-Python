from random import randint

numero = randint(0, 9999)

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'O numero sorteado foi {numero}\
      \nMilhar » {milhar}\
      \nCentena » {centena}\
      \nDezena » {dezena}\
      \nUnidade » {unidade}')