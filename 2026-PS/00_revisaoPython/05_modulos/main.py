'''
Sistema de conversão de inidades

diciplina : Programação de Sistemas {PS}
aula : D7 - Revisão: Modulos
Autor : Renan Soares da Silva
data: 05.03.2026
repositorio: https://github.com/MODEKAISER-renan/Atividadades-e-trabalhos
'''

from conversores import(
    celsius_para_fahrenheit,celsius_para_kelvin,fahrenheit_para_celsius,
    km_para_milhas,milhas_para_km,metros_para_pes
)

from utils import cabecalho_secao,formatar_resultado,linha_separadores

def menu_temperatura():
    print(cabecalho_secao("Conversão de Temperatura"))
    valor = float(input("Valor em C"))
    print(formatar_resultado("C - F", valor, "C", celsius_para_fahrenheit(valor), "F"))
    print(formatar_resultado("C - K", valor, "C", celsius_para_kelvin(valor), "K"))

def menu_distancia():
    print(cabecalho_secao("Conversão de Distância"))
    valor = float(input("Valor em km"))
    print(formatar_resultado("km - mi", valor, "km", km_para_milhas(valor), "mi"))
    print(formatar_resultado("Km - pés", valor * 1000, "m", metros_para_pes(valor * 1000), "pés"))

def main():
    print(linha_separadores())
    print("SISTEMA DE CONVERSÃO DE UNIDADES")
    print(linha_separadores())

    opcoes = {"1":menu_temperatura,"2":menu_distancia}

    while True:
        print("\n[1] Temperatura [2] Distancia [0] Sair")
        escolha = input("Opção:").strip()
        if escolha == "0":
            print("\nSistema encerrado.")
            break
        elif escolha in opcoes:
            opcoes[escolha]()
        else:
            print(" Opção invalida.")
if __name__ == "__main__":
    main()