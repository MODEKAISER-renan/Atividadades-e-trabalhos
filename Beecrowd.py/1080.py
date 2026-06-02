'''
Data inicial: 05.05.2026
data final: 05.05.2026
'''

maior = 0
possicao = 0

for i in range(1,101):
    entrada = int(input())
    if entrada > maior:
        maior = entrada
        possicao = i

print(maior)
print(possicao)