'''
data: 25.04.2026
data final: 25.04.2026
'''

lista = []
numero2 = ""
verificador = 0

repeticao = int(input())

for i in range(repeticao):
    msg =  []
    numero = int(input())
    if numero % 2 == 0:
        msg += ["EVEN "]
    else:
        msg += ["ODD "]
    if numero > 0:
        msg += ["POSITIVE"]
    else:
        msg += ["NEGATIVE"]
    if numero == 0:
        msg = ["NULL"]
    lista += msg

for numero in lista:
    if numero == "NULL":
        print(numero)
    else:
        numero2 += numero
        verificador += 1
    if verificador == 2:
        print(numero2)
        verificador = 0
        numero2 = ""