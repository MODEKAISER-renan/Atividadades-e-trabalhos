'''
===========================================================
Sistema de bibiteca
===========================================================
Disciplina: Porgramação de sistemas (PS)
Aula: 06-Revisão: Funcões
Autor: Renan soares da Silva
Data: 03.03.2026
Repositorio: https://github.com/MODEKAISER-renan/Atividadades-e-trabalhos
===========================================================
Descrição:
calcular e classificar o IMC de uma pessoa
Dempsntar definição de funções, parâmetros,
retorno, escopo e recursão
'''

#Funções sem parâmetro e sem retorno

def exibir_cabecalho():
    print("*"*40)
    print("      SISTEMA DE CÁLCULO D EIMC")   
    print("*"*40)
def comando_final():
    print("*"*40)
    print(" "*10,"  SISTEMA \n", " "*10 ,"FINALIZADO ")   
    print("*"*40)
def calcular_imc(peso, altura):
    imc = peso/(altura**2)
    return imc
def demonstrar_escopo():
    msg = "Olá do interir da função"
    print("Dentro da fnção")
    print(f"mensagem = {msg}")
    print(f"versão = {versao}")
def classificar_imc(imc,unidade='kg/m2'):
    if imc <18.5:
        classificacao = "Abaixo do peso"
        emoji = ":("
    elif imc < 25.0:
        classificacao = "peso normal"
        emoji = ":)"
    elif imc < 30.0:
        classificacao = "Acima do peso"
        emoji = ":["
    else:
        classificacao = "Obeso"
        emoji = ":o"
    return classificacao,emoji
def contagem_regressiva(n):
    if n < 0:
        return
    print(n)
    contagem_regressiva(n - 1)

def processar_pessoa():
    nome = input("\nNome:")
    peso = float(input("Peso (Kg):"))
    altura = float(input("Altura (m):"))
    resultado = calcular_imc(peso,altura)
    print(f"Seu IMC é: {resultado:.2f}")
    classificacao, emoji = classificar_imc(resultado)
    print(f"IMC {resultado:.2f} {classificacao} {emoji}")

versao = "1.0"

exibir_cabecalho()

contiunar = 's'

while contiunar == 's':
    processar_pessoa()
    contiunar = input("\nProcessar mais alguma pessoa?\ns/n: ").lower()

print("CONTAGE REGRESSIVA PARA FINALIZAR O CÓDIGO")
contagem_regressiva(5)

comando_final()
