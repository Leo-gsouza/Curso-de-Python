import random

aluno1 = str(input('Nome do 1º Aluno: ')).capitalize()
aluno2 = str(input('Nome do 2º Aluno: ')).capitalize()
aluno3 = str(input('Nome do 3º Aluno: ')).capitalize()
aluno4 = str(input('Nome do 4º Aluno: ')).capitalize()

alunos = [aluno1, aluno2, aluno3, aluno4]

ordem = random.shuffle(alunos)

print(f'A ordem sorteada pelo professor foi {alunos}')