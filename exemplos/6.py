soma = 0
vezes = 0
resposta ='s'

while resposta =='s' or resposta=='S':
    num = float(input('Digite um numero: '))
    soma = soma + num
    vezes = vezes + 1
    media = soma/vezes
    resposta = input('Deseja continuar(S/N): ')
print(media)