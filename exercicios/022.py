
nome = str(input('Nome completo: ')).capitalize().strip()

print(f'Nome em letra maiuscula » {nome.upper()}')
print(f'Nome em letra minuscula » {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras ')

""" USANDO LISTA PARA SEPARAR O NOME """

nome_separado = nome.split()

print(f'Seu primeiro nome é {nome_separado[0]} e tem {len(nome_separado[0])} letras')