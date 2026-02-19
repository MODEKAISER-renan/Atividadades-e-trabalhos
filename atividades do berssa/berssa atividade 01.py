cont = 1
valor = 0
valor2 = 0
saida = 0
ax = 0
msg = ()
opcoes = ()

def soma(valor,valor2):
        print("o resultado da operação é = ",valor + valor2)
def subtração(valor,valor2):
        print("o resultado da operação é = ",valor - valor2)
def multiplicacao(valor,valor2):
        print("o resultado da operação é = ",valor * valor2)
def msgs(msg):
        cont2 = 0
        for i in (msg):
                print(f"*{msg[cont2]}*\n")
                cont2 += 1
def vx(opcoes): # sistema de verificação expecifico
        global ax
        cont = 1
        while cont == 1:
                try:
                        ax = int(input("digite a sua opção: "))
                except:
                        print("digite um numero:")
                else:
                        if ax in opcoes:
                                cont = 0
                                print("Opção valida")
                                return ax
                        else:
                                print("Opção invalida")
def verificaoN(msg):
       global saida
       cont = 1
       while cont == 1:
                try:
                       saida = int(input(msg))
                except:
                       print("Digite um número:")
                else:
                       cont = 0
                       print("Opção valdia")
                       return saida

while cont == 1:
    msg = [" o que quer fazer? ","somar[1]","subtrair[2]","multiplicação[3]","nenhuma das opções(terminar o código)[4]"]
    msgs(msg)
    opcoes = (1,2,3,4)
    vx(opcoes)
    if ax == 4:
          cont = 0
          break
    msg = "digite o valor 1:"
    verificaoN(msg)
    valor = saida
    msg = "digite o valor 2:"
    verificaoN(msg)
    valor2 = saida
    if ax == 1:
        soma(valor,valor2)
    if ax == 2:
        subtração(valor,valor2)
    if ax == 3:
       multiplicacao(valor,valor2)
print("Agradeço por usar esse código")