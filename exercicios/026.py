
frase = str(input('Digite uma frase: ')).strip().lower()
frase = frase.replace(' ', '')


letra_a = 'a' in frase

if letra_a:
    print(f'A frase contém {frase.count("a")} letras A\
          \nA 1ª letra A se encontra na {frase.find("a")+1}ª posição \
          \nA ultima letra A se encontra na {frase.rfind("a")+1}ª posição')
else:
    print(f'A frase digitada não contem a letra "a" .')