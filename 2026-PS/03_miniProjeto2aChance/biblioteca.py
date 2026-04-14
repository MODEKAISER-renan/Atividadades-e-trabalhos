'''

Diciplina: Programação de Sistemas

Aula: Aula 12 e 13: Mini-projeto Integrador de Lógica e Paradigma Estruturado - Parte 1 e Parte 2

Integrantes: Renan Soares da Silva, Ana Vitoria Schactae Brandao, João Pedro oliveira

Descrição: É um Sistema de armanezamento de dados simples para um pequeno Sebo onde ele guarda as informações que recebe em dados.txt e marca o horario de cada ação em historico.txt, esse sistema guardas as infromções  da seguinte forma "Nome,quantidada,preco" e da a disponibilidade de adicionar um valor, modificar ou retirar ele, além de ter um sistema de busca e salvalemto automatico toda vez que o código é finalizado da forma correta (selecionar a opção para sair).

'''

""" -- 1 TIPOS DE DADOS E VARIÁVEIS --
Uso de pelo menos três tipos distintos (string, int, float ou bool) com nomes de variáveis significativos e adequados ao problema

linha 77 - variável nome tipo string (texto)
linha 154 - variável quantidade tipo int (números inteiros)
linha 155 - variável preco tipo float (número com casas decimais)
linha 148 - variável verificacao usada como controle (tipo string, funciona tipo um "achou ou não")
"""

""" -- 2 OPERADORES --
Operadores aritméticos, relacionais e lógicos presentes em funcionamento

linha 161 - operador aritmético (preço - 10 e preço + 10 para criar intervalo)
linha 54 - operador relacional (valor > 0)
linha 51 - operador lógico (while True, continua enquanto for verdadeiro)
linha 160 - operadores juntos (>= e <= com and para verificar faixa de preço)
"""

""" -- 3 ESTRUTURAS DE DECISÃO --
Uso de if/elif/else para controlar o fluxo do programa

linha 149 até 172 - controla o tipo de busca (nome, quantidade ou valor)
linha 222 até 241 - controla o menu, dependendo da opção escolhida pelo usuário
"""

""" -- 4 ESTRUTURAS DE REPETIÇÃO ---
Uso de while e for

while:
linha 204 - loop do menu (fica rodando até o usuário sair)
linha 146 - loop da busca (permite fazer várias buscas)

for:
linha 15 - percorre os itens para salvar no arquivo
linha 24 - percorre o arquivo para carregar os dados
linha 95 - percorre a lista para mostrar os produtos
linha 108, 121, 151 - percorre a lista para remover, atualizar e buscar

while foi usado para repetir o sistema
for foi usado para percorrer listas e arquivos
"""

""" -- 5 FUNÇOES --
Funções criadas e o que cada uma faz

linha 13 - salvar_dados: salva os dados no arquivo dados.txt
linha 20 - carregar_dados: carrega os dados do arquivo
linha 30 - registrar_historico: salva as ações com data e hora
linha 34 - verificacao_numerica: verifica se o valor digitado é válido

linha 62 - Cadastrar_item: cadastra novos produtos
linha 90 - Listar_item: mostra os produtos
linha 95 - Remover_item: remove um produto
linha 106 - Atualizar_item: atualiza quantidade ou preço
linha 125 - estatiticas_do_sistema: mostra dados gerais
linha 134 - busca: faz busca de produtos
linha 200 - menu: controla o sistema inteiro

cada função tem sua responsabilidade separada
"""

""" -- 6 try/except --
Usado para evitar erros no programa

linha 21 - erro ao abrir arquivo
linha 52 - erro ao digitar número
linha 82 - erro na conversão de quantidade/preço
linha 214 - erro ao escolher opção do menu

isso evita que o programa quebre
"""

""" -- 7 ARQUIVOS --
Uso de arquivo .txt para salvar dados

linha 13 - salva os dados no arquivo
linha 20 - carrega os dados do arquivo
linha 30 - salva histórico das ações

o sistema salva quando fecha, assim os dados não são perdidos
"""

from datetime import datetime
import time

Lista_de_itens = []

def salvar_dados():
    with open("2026-PS/03_miniProjeto2aChance/dados.txt", "w", encoding="utf-8") as f:
        for p in Lista_de_itens:
            linha = f"{p['nome']};{p['quantidade']};{p['preco']};{p['categoria']}\n"
            f.write(linha)

def carregar_dados():
    try:
        with open("2026-PS/03_miniProjeto2aChance/dados.txt", "r", encoding="utf-8") as f: 
            for linha in f:
                partes = linha.strip().split(";")
                if len(partes) == 4:
                    nome, quantidade, preco, categoria = partes
                    Lista_de_itens.append({
                        "nome": nome,
                        "quantidade": int(quantidade),
                        "preco": float(preco),
                        "categoria": categoria
                    })
    except FileNotFoundError:
          print("Arquivo não encontrado, criando novo arquivo.")
    
def registrar_historico(texto): 
    with open("2026-PS/03_miniProjeto2aChance/historico.txt", "a", encoding="utf-8" ) as arquivo:
        arquivo.write(f"{datetime.now()} - {texto}\n")

def verificacao_numerica(nome="valor",opcoes = [],lista_de_opçoes = ''):
    if len(opcoes) == 0: 
        while True:
            try:
                valor = float(input(f"Digite {nome}: "))
                if valor > 0:
                    print(f"{nome} valido.")
                    return valor
                else:
                    print(f"{nome} invalido, tente novamente")
                    continue 
            except Exception as e:
                print(f"Erro inesperado {e}")
                continue
    else:
        while True:
            try:
                opcao = input(lista_de_opçoes)
                for categoria in opcoes:
                    if opcao.lower() in categoria.lower():
                        return opcao
                print("Opção invalida")
            except Exception as e:
                print(f"Erro inesperado {e}")

def Cadastrar_item():
    categoria = verificacao_numerica(opcoes=["CD","Jogos","Livros"],lista_de_opçoes="Escolha a categoria.\nCD\nLivro\nJogos\n")
    nome = input("Digite o nome do produto: ")
    for produto in Lista_de_itens:
        if nome.lower() in produto["nome"].lower():
            print("Produto já cadastrado!")
            return
    try:
        quantidade = int(verificacao_numerica(nome="quantidade"))
        preco = verificacao_numerica(nome="preço")
    except:
        print("Preço inválido!")
        return
    Lista_de_itens.append({
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco,
        "categoria":categoria
    })
    print("Produto cadastrado!")
    registrar_historico(f"Produto cadastrado: {nome}")

def Listar_item():
    for produto in Lista_de_itens:
        print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R$ {produto['preco']:.2f}, Categoria: {produto['categoria']}")
    registrar_historico(f"Produtos listados")

def Remover_item():
    item = input("Digite o nome do produto que quer remover:").lower()
    for produto in Lista_de_itens:
        if item in produto["nome"].lower():
            Lista_de_itens.remove(produto)
            print(f"Produto '{produto['nome']}' removido.")
            registrar_historico(f"Produto removido: {produto['nome']}")
            break
    else:
        print("Produto não encontrado.")

def Atualizar_item():
    item = input("Digite o nome do produto que quer atualizar: ").lower()
    for produto in Lista_de_itens:
        if item in produto["nome"].lower():
            escolha1 = input("deseja atualizar a quantidade do produto? (s/n): ").lower()
            escolha2 = input("deseja atualizar o preço do produto? (s/n): ").lower()
            if escolha1 == "s":
                nova_quantidade = int(verificacao_numerica(nome="quantidade"))
                produto["quantidade"] = nova_quantidade
            if escolha2 == "s":
                novo_preco = verificacao_numerica(nome="preço") 
                produto["preco"] = novo_preco
            print(f"Produto '{produto['nome']}' atualizado.")
            registrar_historico(f"Produto atualizado: {produto['nome']}")
            break
    else:
        print("Valor não encontrado.")

def estatiticas_do_sistema():
    estatiticas = {"itens_distintos":0,"total_de_itens":0,"valor_total":0}
    for produto in Lista_de_itens:
        estatiticas["itens_distintos"] += 1
        estatiticas["total_de_itens"] += produto["quantidade"]
        estatiticas["valor_total"] += produto["preco"]*produto["quantidade"]
    print(f"Quantidade de itens diferentes: {estatiticas['itens_distintos']}\nTotal de itens: {estatiticas['total_de_itens']}\nValor total de todos os itens: {estatiticas['valor_total']:.2f}")

def busca():
    while True:
        verificacao = "n"
        print("\n=== BUSCA DE ITENS ===")
        print("[1] Buscar por nome")
        print("[2] Buscar por quantidade de itens.")
        print("[3] Buscar por valor aproximado.")
        print("[4] Finalizar busca.\n")
        resposta = verificacao_numerica(nome="a opção que deseja")

        if resposta == 1:       
            nome = input("Escreva o nome do produto: ").lower()
            for produto in Lista_de_itens:
                if nome in produto['nome'].lower():
                    verificacao = "s"
                    print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R$ {produto['preco']:.2f}")

        elif resposta == 2:
            quantidade = int(verificacao_numerica(nome="Item da busca"))      
            for produto in Lista_de_itens:
                if quantidade == produto['quantidade']:
                    verificacao = "s"
                    print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R$ {produto['preco']:.2f}")

        elif resposta == 3:
            valor = verificacao_numerica(nome="Valor do item")
            for produto in Lista_de_itens:
                if valor  >= produto['preco'] - 10 and valor <= produto['preco'] + 10:
                    verificacao = "s"
                    print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R$ {produto['preco']:.2f}")
        elif resposta == 4:
            print("Finalizando busca...\n")
            break
        if verificacao == "n": 
            print("Item não encontrado/Opção invalida\n")
            registrar_historico("Busca sem resultado")
        else:
            print("\nBusca feita com sucesso!\n")
            registrar_historico("Busca realizada")

def menu():
    while True:
        print("\n📋 MENU")
        time.sleep(0.5)
        print("1 - Cadastrar item")
        print("2 - Listar itens")
        print("3 - Atualizar quantidade")
        print("4 - Remover item")
        print("5 - Buscar por item")
        print("0 - Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida! Digite um número.")
            continue
        
        if opcao == 1:
            Cadastrar_item()
        elif opcao == 2:
            Listar_item()
        elif opcao == 3:
            Atualizar_item()
        elif opcao == 4:
            Remover_item()
        elif opcao == 5:
            busca()
        elif opcao == 0:
            salvar_dados()
            estatiticas_do_sistema()
            for i in range(3, 0, -1):
                print(f"O programa fechara em: {i} ", end="\r")
                time.sleep(0.5)
            print("Fechando agora!\nObrigado por usar...")
            break
        else:
            print("Opção inválida!")
            
if __name__ == "__main__":
    for i in range(5, 0, -1):
            print(f"O programa iniciará em: {i} ", end="\r")
            time.sleep(1)
    print("\n"*50)
    carregar_dados()
    menu()