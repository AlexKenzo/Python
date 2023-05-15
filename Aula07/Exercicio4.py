positivos = 0
negativos = 0
menor = float('inf')

while True:
    valor = float(input('Digite um valor ou digite 0 para sair: '))
    if valor == 0:
        break
    if valor < menor:
        menor = valor
    if valor > 0:
        positivos +=1
    else:
        negativos+=1

print('Positivos: {}\nNegativos: {}\nMenor: {}'.format(positivos,negativos,menor))
