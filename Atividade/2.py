num = input('Digite um número inteiro com três algarismos: ')
inverso = num[::-1]
soma = int(num) + int(inverso)
print(f'O inverso do número é: {inverso}\nA soma é: {num} + {inverso} = {soma}')
