# Arquivo: 01b-debug.py
#Atenção: Esse códgio cntem 4 erros propositais. encontre e corrija.
nome = input("Digite o nome do aluno: ") # Primeiro erro, o código "input" estava escrit errado ( no caso tava escrito como "imput")
nota1 = float(input("digite a nota 1:"))
nota2 = float(input("digite a nota 2:"))

media = (nota1+nota2)/2 #outro erro, a soma das notas estava fora dos "()", se fosse feita sem os "()" primeiro iria dividir a nota2 e depois somar com a nota1, o correto é somar as duas notas e depois dividir
if media >= 6.0:
    sitacao = "Aprovado"
elif media >= 4.0:
    situacao = "Recuperação"
else: #a correção foi no espassamento que estava equivocado fazend o sistema não  ler o else.
    situacao = "reprovado"
print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}") #ultimo erro, em vez de "print" estava escrito "pronyo".