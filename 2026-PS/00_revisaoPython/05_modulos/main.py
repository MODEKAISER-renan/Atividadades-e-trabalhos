'''
Sistema de conversão de inidades

diciplina : Programação de Sistemas {PS}
aula : D7 - Revisão: Modulos
Autor : Renan Soares da Silva
data: 05.03.2026
repositorio: https://github.com/codespaces?repository_id=1161897302
'''

# bloco1 : STDBIB
import math
from random import randint,choice
from datetime import datetime

from conversores import temperatura

from conversores import km_para_milhas, celsius_para_fahrenheit

print("Exploradores a Stdlib")
print(f"n = {math.pi:.4f}")
print(f"(raiz²)2 = {math.sqrt(2):.4f}")
print(f"Búmero aleatorio: {randint(1,100)}")
print(f"Unidde sorteada: {choice(["km","milhas","metros"])}")
print(f"Agora: {datetime.now().strftime("%d/%m/%Y %H:%M")}")

print("\n === conversão de Temperatura")
valor = 100.0
print(f"{valor}*C = {temperatura.celsius_para_fahrenheit(valor):.1f}*F")
print(f"{valor}*C = {temperatura.celsius_para_kelvin(valor)} K")
print(f"Zero absoluto: {temperatura.ZERO_ABSOLUTO_CELSIUS}*C")

print("\n === API Limpo ===")
print(f"100 km = {km_para_milhas(100):.2f}milhas")
print(f"25 C = {celsius_para_fahrenheit(25):.1f} F")