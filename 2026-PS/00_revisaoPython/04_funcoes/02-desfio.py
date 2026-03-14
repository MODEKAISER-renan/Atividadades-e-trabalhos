"""
Nome: Renan Soares da Silva
Data: 12.03.2026
Diciplina:Desenvolvimento de Sistemas

Descrição: Fazer um sistema de escola utilizando funções em grande parte que leia e verifique a situação de alunos
"""
# lugar onde vou trabar com os dados que o código for gerando
Turma = [
    {"Aluno":"Camila","Nota1":8,"Nota2":6,"Media":0,"Situacao":""},
    {"Aluno":"Renan","Nota1":9,"Nota2":2,"Media":0,"Situacao":""},
    {"Aluno":"Rafaela","Nota1":4,"Nota2":3,"Media":0,"Situacao":""}
]
#banco de dados que gurda as informações de quantos foram aprovados, recuperção ou reprovados
Lista_situacao_dos_alunos = {
        "Aprovados":0,
        "Recuperacao":0,
        "Reprovado":0
    }

#criação de uma varial lista para futuramente calcular a meida geral
Lista_de_medias = []

#Calcula a media de um unico aluno
def media_de_notas(nota1,nota2):
    media = (nota1+nota2)/2
    return media

#Com base na media faz a verificação da situação do aluno
def situacao_aluno(media):
    if media >= 6.0:
        situacao = "Aprovado"
    elif media < 4.0:
        situacao = "Reprovado"
    else:
        situacao = "Recuperacao"
    return situacao

#Verifica se a entrada do usuario é u numero e se é um numero entre 0 e 10
def verificacao():
    while True:
        try:
            nota = float(input("Digite a nota do aluno: "))
            if nota > 10 or nota < 0:
                print("Nota invalida, tente novamente")
            else:
                return nota
        except:
            print("Valor invalido, tente novamente")

#pega as informações que vieram do input e organiza elas para que possa ser enviada para o usuario de forma clara           
def relatorio(Nome,Media,Situacao):
    print(f"Nome do aluno: {Nome}\nMedia do aluno: {Media}\nSitução do aluno: {Situacao}")

#Usa todas as funções anteriores para verificar a entrada, fazer a media, ver a situação e por fim dar o relatorio do aluno
def cadrastro_aluno():
    nome = input("Digite o nome do aluno: ")
    nota1 = verificacao()
    nota2 = verificacao() 
    media = media_de_notas(nota1,nota2)
    situacao = situacao_aluno(media)
    Turma.append(
        {"Aluno":nome,"Nota1":nota1,"Nota2":nota2,"Media":media,"Situacao":situacao}
    )
    relatorio(nome,media,situacao)

#É parecido com o cadrasto, porém esse código apenas mostra o nome, media e a situação do aluno que já estão cadastrados, todos sem exessão
def lista_de_todos_os_alunos():
    for aluno in Turma:
        media = media_de_notas(aluno["Nota1"],aluno["Nota2"])
        situacao = situacao_aluno(media)
        aluno["Media"] = media 
        aluno["Situacao"] = situacao 
        relatorio(aluno["Aluno"],aluno["Media"],aluno["Situacao"])

#Calcula, a traves da lista já feita,a media de toda a turma e depois retorna esse mesmo valor.        
def calcular_media_turma(divisor=0,total_nota=0.0):
        if divisor == len(Lista_de_medias):
            media_geral = total_nota/divisor
            return media_geral
        else:
            total_nota += Lista_de_medias[divisor]
            divisor += 1
            return calcular_media_turma(divisor,total_nota)

#Resposta final do sistema, ele guardaos aprovados, em recuperação e os reprovados e depois retorna esse mesmo valor
def resumo_turma():
    Lista_situacao_dos_alunos["Aprovados"] = 0
    Lista_situacao_dos_alunos["Reprovado"] = 0
    Lista_situacao_dos_alunos["Recuperacao"] = 0
    for alunos in Turma:
        if alunos["Situacao"] == "Aprovado":
            Lista_situacao_dos_alunos["Aprovados"] += 1
        if alunos["Situacao"] == "Recuperacao":
            Lista_situacao_dos_alunos["Recuperacao"] += 1
        if alunos["Situacao"] == "Reprovado":
            Lista_situacao_dos_alunos["Reprovado"] += 1
    return Lista_situacao_dos_alunos

#Código realmente funcioando
while True:            
    cadrastro_aluno()
    lista_de_todos_os_alunos()
    #detalhe importante, aqui é a criação de lista que é usado para calcular a media da turma
    Lista_de_medias = []
    for aluno in Turma:
        Lista_de_medias.append(aluno["Media"])
    media_geral = calcular_media_turma()
    print(f"Meida geral da turma: {media_geral:.1f}")
    resumo_turma()
    #e aqui é usado os valores que vem do resumo_turma
    print(f"Alunos Aprovados: {Lista_situacao_dos_alunos['Aprovados']}\nEm recuperação: {Lista_situacao_dos_alunos['Recuperacao']}\nReprovados: {Lista_situacao_dos_alunos['Reprovado']}")
    resposta = input("deseja repetir este código? s/n: ")
    if resposta != "s":
        break