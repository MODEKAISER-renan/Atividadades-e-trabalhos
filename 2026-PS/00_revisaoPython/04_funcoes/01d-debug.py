def saudacao(nome,turno="manhã"):
    msg = f"Bom {turno}, {nome}!"
    return msg #faltou declar que o valor deve retornar

saudacao('Ana') # meio inutil isso aqui né
print(saudacao("Bruno","tarde"))

def dorbar(x):
    resultado = x * 2
    return resultado # novamente faltou o reunt, sem ele nenhum valor retorna e deixa o código totalmente inutil
print("Dobro de 5:",dorbar(5))

total = 0
def incrementar():
    global total 
    total = total + 1 # o erro do código está aqui, pracorrigir primero tive que adicionar o temo global, pq não tem como uma função modificar uma variavel fora dela sem que tenha a "permissão", e o segundo erro é que não tem  retur, logo o valor se perde
    return total
incrementar()
print("total:",total)

def contagem(n):
    if n < 0: # faltou o sistema de verificação para que o código tivesse fim, sem ele vira um loop infinito
        return
    print(n)
    contagem(n-1)
contagem(3)