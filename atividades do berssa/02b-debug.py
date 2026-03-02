#Arquivo: 02b-debug.py
#contem 04 erros, corrija todos
catalogo = [
    {"titulo":"Código Limpo","autor":"Robert C. Martin","disponivel":True},
    {"titulo":"Entendendo Agoritimo","autor":"Aditya Bharrgava","disponivel":False},
    {"titulo":"pythin Flutuante","autor":"Luiano Ramalho","disponivel":True},
]

print("Primeiro livro:",catalogo[0]["titulo"]) # catlogo[3] esta fora do range além de que não pegaria o primeiro liro, para isso deveria ser 0

print('\nLivros disponiveis:')
for livro in catalogo:
    if livro['disponivel'] == True: # o valor estava invertido, fazendo que só mostrasse os livros que não tivesem disponiveis, trocando o "False" por "True" o código fois reparado
        print(f'sim {livro['titulo']}')

total = len(catalogo)
print(f'\nTotal de livros: {total}')
for chave,valor in catalogo[0].items(): # faltou o ".items()para declarar para o sistema que é mais de uma opção"
    print(f' {chave}:{valor}')
primeiro_autor = catalogo[0]['autor']# originemente tava escrito "Autor", isso é errado por que no catalogo esta escrito "autor" fazendo que quando fosse fazer a busca desse erro.
print('\nAutor do primeiro livro:',primeiro_autor)

#comit finalizado