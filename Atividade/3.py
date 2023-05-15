palavra = str.upper(input('Entre com uma string: '))
frequencia = {}
for caracter in palavra:
    if caracter in frequencia:
        frequencia[caracter] +=1
    else:
        frequencia[caracter] = 1

for caracter, contador in frequencia.items():
    print(f'O caractere {caracter} aparece {contador} vezes')