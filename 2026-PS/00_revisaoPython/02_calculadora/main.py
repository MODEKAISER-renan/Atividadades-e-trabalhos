#Variaves previamente declaradas
cont = 1
valor = 0
valor2 = 0
saida = 0
ax = 0
msg = ()
opcoes = ()
#funções de operação e verificação
def soma(valor,valor2):# soma os dois valores e depois os mostra na tela
        print("o resultado da operação é = ",valor + valor2)
def subtração(valor,valor2):#diminui dois valores e após mostra na tela
        print("o resultado da operação é = ",valor - valor2)
def multiplicacao(valor,valor2):#multiplca dois valores e após mpstra na tela
        print("o resultado da operação é = ",valor * valor2)
def divisao(valor,valor2):# tenta dividir dois valroes, caso de certo mostra o resultado da divisão na tela, caso de errado fala que não é possivel dividir por 0 (já que é a unica divisão numerica que pode dar erro de divisão)
        try:
               print("o resultado da operação é = ",valor / valor2)
        except:
               print("não é posivel dividir por zero")

def msgs(msg):# apóes receber as msg pela variavel "msg" mostra todas as msg em sequencia
        cont2 = 0
        for i in (msg):
                print(f"*{msg[cont2]}*\n")
                cont2 += 1
def vx(opcoes): # sistema de verificação expecifico numerico
        global ax
        cont = 1
        while cont == 1:# laço de repetição usado para fazer a verificação quantas vezes for necessario
                try:#tenta execuatr o código para receber o numero do teclado.
                        ax = int(input("digite a sua opção: "))
                except:#em caso de erro manda uma msg para o usuario faladno que a entrada é invalida(no caso não é um numeral)
                        print("digite um numero:")
                else:#caso de certo ele ira verificar dentro de opções se o numero que foi digitado tem entre as opçoes, caso aja, ele ira quebrar o laço de repetição e retornar o valoro de entrada, caso não, dira que a entrada é invalida e forçara o usiario digitar uma entrada valida
                        if ax in opcoes:
                                cont = 0
                                print("Opção valida")
                                return ax
                        else:
                                print("Opção invalida")
def verificaoN(msg):#sistema de verificação abrangente numerico
       global saida
       cont = 1
       while cont == 1:#laço de reétição 
                try:#tenta receber um valor numerico do usuario
                       saida = int(input(msg))
                except:#em caso de erro manda a mensagem de erro e volta o laço de repetição
                       print("Digite um número:")
                else:#caso não tenha erro nenhum ele ira dizer que teve uma opção valida e ira retornar o valor de entrada
                       cont = 0
                       print("Opção valdia")
                       return saida
#código realmente funcionando
while cont == 1:#laço principal de repetição(coração do código)
        msg = [" o que quer fazer? ","somar[1]","subtrair[2]","multiplicação[3]","Divisão[4]","nenhuma das opções(terminar o código)[5]"]#msg que irão ser enviadar ao usuario
        msgs(msg)#ação de chamar a funão msg que envia as msg para o usuario
        opcoes = (1,2,3,4,5)#as opções que deverão ser testadas pela função"vx(opcoes)
        vx(opcoes)#chamando a função opcoes
        if ax == 5:#caso o valor que veio da função vc(opcoes), irá encerrar o código
                cont = 0
                break
        msg = "digite o valor 1:"#msg que devera ir ao usuario
        verificaoN(msg)#função qe manda a msg para o usuario e retorna um valor do usuario
        valor = saida # valor que voltou do usuario snedo reorganizado 
        msg = "digite o valor 2:"#msg que deve ir ao usuario
        verificaoN(msg)#função qe manda a msg para o usuario e retorna um valor do usuario
        valor2 = saida # valor que voltou do usuario snedo reorganizado
        #os casos de teste para veirifcar e chamar a opração de acorodo com a escolha do usuario
        if ax == 1:
                soma(valor,valor2)
        if ax == 2:
                subtração(valor,valor2)
        if ax == 3:
                multiplicacao(valor,valor2)
        if ax == 4:
                divisao(valor,valor2)
#msg final do código
print("Agradeço por usar esse código")