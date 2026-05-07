'''
data inivial: 05.05.2026
data final:
'''

coelhos = 0
ratos = 0
sapos = 0
total_testes = 0
''
entrada = int(input())

for i in range (entrada):
    qnt_testes,animal = input().split()
    qnt_testes = int(qnt_testes)
    if animal == "C":
        coelhos += qnt_testes
    elif animal == "R":
        ratos += qnt_testes
    elif animal == "S":
        sapos += qnt_testes
    total_testes += qnt_testes

print(f"Total: {total_testes} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {(coelhos*100)/total_testes:.2}")
print(f"Percentual de ratos: {(ratos*100)/total_testes:.2}")
print(f"Percentual de sapos: {(sapos*100)/total_testes:.2}")