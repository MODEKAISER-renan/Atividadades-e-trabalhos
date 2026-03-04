'''
===========================================================
Sistema de bibiteca
===========================================================
Disciplina: Porgramação de sistemas (PS)
Aula: 05-Revisão: Estruras de dados
Autor: Renan soares da Silva
Data: 26.02.2026
Repositorio: https://github.com/MODEKAISER-renan/Atividadades-e-trabalhos
===========================================================
Descrição:
Cayálogar de livros que demonstra o uso de listas e dicionarios para armazenar, onsultar  e filtrar dados estruturis.
'''
# Listas: conceitos básicos

#Crinando uma lista de titulos
titulos = [
    'O Porgramador Pragmático',
    'Código Limpo',
    'Entendendo Algoritimos',
]
#Acesso pr indice (cmeça em 0, não em 1!)
print("Primeito livro:",titulos[0])
print("Ultimo livro:",titulos[-1])
print("Todos os Livros:",len(titulos))
#Metodos de Lista
print("\n---operações na Lista")

#Adicinar um item ao final
titulos.append("Phyton Flutuante")
print("Após append:",titulos)

# Verificar se item existe
buscar = "Código Limpo"
if buscar in titulos:
    print(f'"{buscar}" está no catalogo.')
else:
    print(f'"{buscar}" não encontrado.')

# ordenar lsita
titulos.sort()
print("Listar ordenadas:", titulos)

#remover um item 
titulos.remove("Entendendo Algoritimos")
print("Após remove:",titulos)

#for a,titulos in enumerate(titulos):
#    print(f"{a} {titulos}")

#icionarios: conceitos básicos
#um dicionário representa um livro com seus atributos
livro = {
    "titulo": "O Programador Pragmático",
    "autor": "Andrew Hunt",
    "ano": 1999,
    "disponível": True,
}
print("Título :",livro["titulo"])
print("Autor :",livro["autor"])
print("Ano :",livro["ano"])
print("Status :","Disponivel"if livro["disponível"] else "Emprestado")

# modificador e consltando

#autorizando um valor existente
livro ["disponível"] = False
print("\nApós empréstimo:",livro["disponível"])
#adicionando uma chave
livro["paginas"] = 352
print("Páginas:",livro["paginas"])

#.get() = acesso seguro: retorna None (ou padrão) se a chave não existir
editora = livro.get("editora","Não informada")
print("Edititora:",editora)
# catalogo: lista de dicionarios
catalogo = [
    {"titulo":"O Programador Pragmático","autor":"Andrew Hunt","ano":1999,"disponivel":True},
    {"titulo":"Código Limpo","autor":"Robert C. Martin","ano":2008,"disponivel":False},
    {"titulo":"Entendendo Algoritimo","autor":"Aditya Bhargava","ano":2016,"disponivel":True},
    {"titulo":"A vida de um Programador","autor":"Renan Soares","ano":1935,"disponivel":True},
]

print ("=== Catálogo da biblioteca===")
print()
#percorrer cada livro com for
cont = 0
disponivel_cont = 0
for livro in catalogo:
    cont += 1
    status = "Disponivel" if livro["disponivel"] else "emprestado"
    print(f" {cont} {livro["titulo"]} ({livro["ano"]})")
    print(f"Autor:{livro["autor"]} | {status}")
    print(" "+"-"*40)
#--- Consultar e filtros

print("\n===Livros disponíveis===")
for livro in catalogo:
    if livro['disponivel']:
        disponivel_cont += 1
        print(f'sim{livro['titulo']}')

        
print('\n===Buscar por titulo===')
buscar = input("digite o titulo (ou parte):").lower()
encontrado = False
for livro in catalogo:
    if buscar in livro["titulo"].lower():
        print(f'Encontrado: {livro['titulo']} - {livro['autor']}')
        encontrado = True
if not encontrado:
    print(' Nenhum livro encontrado com esse termo.')


print('\n===Atributos do primeiro livro===')
for chave,valor in catalogo[0].items():
    print(f'{chave}:{valor}')
print("Disponiveis =",disponivel_cont,"\nIndisponiveis = ",(cont - disponivel_cont))