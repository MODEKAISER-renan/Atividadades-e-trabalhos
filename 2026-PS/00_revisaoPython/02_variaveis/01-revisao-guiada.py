'''
================================================================================
Sistema de aprovação de Alunos
================================================================================
diciplina: Programação de sistemas {PS}
aula: 04-Revisão:Variaveis,Tipos e Controles de Fluxo
autor: Renan Soares da Silva
data: 24/02/2026
repositorio: https://github.com/MODEKAISER-renan/Atividadades-e-trabalhos
================================================================================

Descrição:

Este progama processa as notas de uma turma e determina a situção de cada aluno (Aprovado,Recuperação ou Reprovação).
Conceitos utilizados: variáveis, tipoes de dados, operados,estrutura de seleção e estruturas de repetição.
================================================================================
================================================================================
                             Processamento
================================================================================
'''
turma = [{"nome":"Ana", "nota1":8.0,"nota2": 7.5},{"nome":"Bruno", "nota1":4.5,"nota2": 5.0},{"nome":"Carla", "nota1":2.0,"nota2": 3.5}
]
print("=== Resultados===")
print()

for aluno in turma:
    nome = aluno["nome"]
    nota1 = aluno["nota1"]
    nota2 = aluno["nota2"]
    media = (nota1 + nota2)/2
    if media >= 6.0:
        situacao = "Aprovado :)"
    elif media >= 4.0:
        situacao = "Recuperação :("
    else:
        situacao = "Reprovado :["
    print(f"Aluno : {nome}")
    print(f"Média : {media:.2f}")
    print(f"Situação: {situacao}")
    print("-"*30)
continuar = "s"
while continuar == "s":
    print("\nDeseja procesar outro aluno? (s/n):",end="")
    continuar = input().lower()
    if continuar == "s":
        nome = input("Digite o nome do aluno:") # entrada do nome do aluno (stg)
        nota3 = float(input("Digite a nota 1 (1 a 10)"))#nota um (valor float)
        nota4 = float(input("Digite a nota 2 (1 a 10)"))#nota dois (valor float)
        media = (nota3+nota4)/2 #calculo da média

        print() # apenas estetico
        print(f"Aluno : {nome}")
        print(f"Nota 1 : {nota3:.1f}")
        print(f"Nota 2 : {nota4:.1f}")
        print(f"Média : {media:.2f}")

        # decisão
        if media >= 6.0:
            situacao = "Aprovado :)"
        elif media >= 4.0:
            situacao = "Recuperação :("
        else:
            situacao = "Reprovado :["
        print(f"Situação : {situacao}")
        print("-" * 40)