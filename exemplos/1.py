num = int(input('Digite um numero: '))
ate1=int(input('Digite um numero que a tabuada irá: '))
ate=ate1 + 1

for i in range(1,ate):
    resultado = num * i
    print('{} x {} = {}'.format(num,i,resultado))