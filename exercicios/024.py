
cidade = str(input('Nome da cidade: ')).strip().title()

print(cidade[0:5] == 'Santo')

""" Condição SE """

if cidade[:5] == 'Santo':
    print(f'Sim! A cidade {cidade} começa com Santo')
else:
    print(f'Não! A cidade {cidade} não começa com Santo')



