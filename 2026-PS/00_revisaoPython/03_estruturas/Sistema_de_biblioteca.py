'''
Nome: Renan Soares da Silva
Diciplina:Desenvolvimento de Sistemas
Data:08.03.2026
Descrição:Fazer um sistema de biblioteca que guarde as infromações dos livros (autor,Titulo,ano,disponivel) com a capacidade de poder manipular essas informações, como ver qual livro está disponivel, procurar um livro pelo nome.
'''

# Area com todas as principasi variaveis
#Biblioteca principal
biblioteca = [
    {"autor":"Emillyn Rank","titulo":"A Descoberta do Submundo","ano":1679,"disponivel":True},
    {"autor":"Lívia Mendes","titulo":"A Morte De Um Cometa","ano":2023,"disponivel":False},
    {"autor":"Camila Ferreira","titulo":"Descoberta da Paixão","ano":2026,"disponivel":True}
]
#bliblioteca de valores, é bem obvio pra que serve
biblioteca_valores = {
    "Livros_disponiveis":0,
    "Livros_emprestados":0
}
# lista todos os livros disponiveis
def Lista_de_livros():
    biblioteca_valores["Livros_disponiveis"] = 0
    biblioteca_valores["Livros_emprestados"] = 0
    for catalogo in biblioteca:
        print(f"Autor: {catalogo["autor"]} Titulo: {catalogo["titulo"]} Ano: {catalogo["ano"]} Estatus: {catalogo["disponivel"]}\n")
        if catalogo["disponivel"] == True:
            biblioteca_valores["Livros_disponiveis"] += 1
        else:
            biblioteca_valores["Livros_emprestados"] += 1
    print(f"Tem {biblioteca_valores['Livros_disponiveis']} livros disponiveis e {biblioteca_valores['Livros_emprestados']} emprestados ")
# A mesma coisa da função anterior só que simplificado só para mandar valores para o banco de valores.
def lista_final():
    biblioteca_valores["Livros_disponiveis"] = 0
    biblioteca_valores["Livros_emprestados"] = 0
    for catalogo in biblioteca:
        if catalogo["disponivel"] == True:
            biblioteca_valores["Livros_disponiveis"] += 1
        else:
            biblioteca_valores["Livros_emprestados"] += 1


#adiciona um livro com todos os dados necessarios de umm livro já no estado disponivel.
def Adicionar_um_titulo():
    biblioteca.append(
        {"autor":input("Digite o Nome do Autor: "),"titulo":input("Digite o Nome do livro: "),"ano":int(input("Digite o ano que foi feito:")),"disponivel":True}
    )
    Lista_de_livros()
#Vai a trás do livro  traves do autor e titulo (caso o autor tenha masi de um livro, tem onome do livro que diferencia)
def Pega_negao():
    autor = input("Digite o nome do Autor: ").lower()
    verificacao = False
    for catalogo in biblioteca:
        if autor in catalogo["autor"].lower():
            print(f"Autor: {catalogo["autor"]} Titulo: {catalogo["titulo"]} Ano: {catalogo["ano"]} Estatus: {catalogo["disponivel"]}")
            verificacao = True
        if not verificacao:
            print("Autor não escontrado, tente novamente")
            Pega_negao()
# Faz que um livro seja emprestado, em resumo, deixa o livro como indisponivel ou dispnivl dependendo do estado atual do livro
def Empresta_negao():
    autor = input("Digite o nome do Autor: ").lower()
    titulo = input("Digite o nome do Titulo: ").lower()
    verificacao = False
    for catalogo in biblioteca:
        if autor in catalogo["autor"].lower() and titulo in catalogo["titulo"].lower():
            catalogo["disponivel"] = not catalogo["disponivel"]
            varificacap = True
            return
    if verificacao != True:
        print("Livro não encontrado, tente novamente")
        Empresta_negao()
#parte final do isstema em si, mostrando os dados finais e finalizando o sistema.
def relatorio_final():
    lista_final()
    print("RELATORIO FINAL\n=============================")
    print(f"Total de Livros disponiveis:{biblioteca_valores["Livros_disponiveis"]}\nTotal de Livros Emprestados:{biblioteca_valores["Livros_emprestados"]}\nTotal de livros: {biblioteca_valores["Livros_disponiveis"] + biblioteca_valores["Livros_emprestados"]}")
    print("Livros emprestados:")
    for catalogo in biblioteca:  
        if catalogo["disponivel"] == False:
            print(f"Autor: {catalogo["autor"]} Titulo: {catalogo["titulo"]} Ano: {catalogo["ano"]} Estatus: {catalogo["disponivel"]}")
            
# o código relamente funcionando e rodando.
while True:
    print("\nBiblioteca digital")
    print("Titulos\n==================")
    Lista_de_livros()
    print("Deseja adicionar um livro? s/n")
    if input("ditite sua resposta: ").lower() == "s":
        Adicionar_um_titulo()
    print("Deseja ver um livro em espesifico? s/n")
    if input("ditite sua resposta: ").lower() == "s":
        Pega_negao()
    print("Deseja emprestar um livro? s/n")
    if input("ditite sua resposta: ").lower() == "s":
        Empresta_negao()
    relatorio_final()
    print("Deseja executat este código novamente? s/n")
    if input("ditite sua resposta: ").lower() != "s":
        break  
#verdadeira menssagem final.
print("Agradeço por usar este código")