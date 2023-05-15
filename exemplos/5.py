numdec = int(input('Digite um numero decimal: '))

binario = ""
while numdec!=0:
    r = numdec%2
    binario = str(r) + binario
    numdec = numdec//2
print(binario)
