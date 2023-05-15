numbin = input('Digigte um numero binario: ')
decimal = 0
n = len(numbin) - 1

for i in numbin:
    decimal = decimal + int(i)*2**n
    n = n -1
print(decimal)