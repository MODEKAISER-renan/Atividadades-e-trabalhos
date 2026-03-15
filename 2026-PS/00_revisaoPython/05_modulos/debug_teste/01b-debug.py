#debug_teste/01-debug.py
# Atenção: há 4 erros propositais. Encontre e corrija todos!
#Rode de dentro de 05_modules/: python debug_teste/01b-debug.py

from conversores import temperatura 

from conversores import celsius_para_kelvin, distancia # não tem converter_distancia, o mais próximo seria importar a distancia em si.
resutlado = celsius_para_kelvin(25)
print(f"25 C em K: {resutlado}")

from utils.formatador import formatar_resultado
print(formatar_resultado("teste", 100, "Km", 62.1, "mi","extra"))

from conversores import km_para_milhas
print(f"50 km - {km_para_milhas(50):.2f}")

from debug_teste import algo

