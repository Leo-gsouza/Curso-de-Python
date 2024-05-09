
nome = str(input('Nome completo: ')).title().strip()

print('Silva' in nome)

if 'Silva' in nome:
    print(f'{nome} tem Silva')
else:
    print(f'{nome} não tem Silva')