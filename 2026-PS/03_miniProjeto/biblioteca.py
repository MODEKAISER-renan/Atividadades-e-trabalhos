'''

Diciplina: Programação de Sistemas

Aula: Aula 12 e 13: Mini-projeto Integrador de Lógica e Paradigma Estruturado - Parte 1 e Parte 2

Integrantes: Renan Soares da Silva, Ana Vitoria Schactae Brandao, João Pedro oliveira

Descrição: É um Sistema de armanezamento de dados simples para um pequeno Sebo onde ele guarda as informações que recebe em dados.txt e marca o horario de cada ação em historico.txt, esse sistema guardas as infromções  da seguinte forma "Nome,quantidada,preco" e da a disponibilidade de adicionar um valor, modificar ou retirar ele, além de ter um sistema de busca e salvalemto automatico toda vez que o código é finalizado da forma correta (selecionar a opção para sair).

'''

""" -- 1 TIPOS DE DADOS E VARIÁVEIS -- USE PELO MENOS TRÊS TIPOS DISTINTOS(STRING, INT, FLOAT OU BOOL) COM NOMES DE VARIÁVEIS SIGNIFICATIVOS E CONTEXTUALMENTE ADEQUADOS AO PROBLEMA
linha 61 - variável opção tipo float(ponto flutuante) 
linha 77 - variável nome tipo string (texto)
linha 154 - variável quantidade tipo int (números inteiros)
"""
""" -- 2 OPERADORES --: OPERADORES ARITMÉTICOS, RELACIONAIS E LÓGICOS PRESENTES EM CONTEXTO FUNCIONAL (NÃO APENAS DECLARADOS)
linha 161 -  operador aritmético (subtração de preço do produto - 10)
linha 54 - operador relacional (se o valor for maior que 0)
linha 51 - operador lógico (enquanto o argumento for verdade)
"""
""" -- 3 ESTRUTURAS DE DECISÃO - APONTE UM BLOCO  if/elif/else E EXPLIQUE QUAL FLUXO ELE CONTROLA
linha 149 até 172 - controla o fluxo de buscas de itens
"""
""" -- 4 ESTRUTURAS DE REPETIÇÃO --- APONTE O LOOP DO MENU E/OU ITERAÇAO SOBRE DADOS; EXPLIQUE QUANDO USOU WHILE E QUANDO USOU FOR E POR QUE
"""
""" -- 5 FUNÇOES -- LISTE AS FUNÇÕES IMPLEMENTADAS E EXPLIQUE A RESPONSABILIDADE DISTINTA DE CADA UMA
linha 29 - salvar_dados é responsável por armazenar no arquivo dados.txt os dados (nome, quantidade, preço e categoria) 
os itens cadastrados
linha 42 - carregar_dados é responsável por transmitir a mensagem de carregamento no início do programa 
linha 68 - verificacao_numerica """ 

from datetime import datetime
import time

Lista_de_itens = []

def salvar_dados():
    with open("2026-PS/03_miniProjeto/dados.txt", "w", encoding="utf-8") as f:
        for p in Lista_de_itens:
            linha = f"{p['nome']};{p['quantidade']};{p['preco']};{p['categoria']}\n"
            f.write(linha)

def carregar_dados():
    try:
        with open("2026-PS/03_miniProjeto/dados.txt", "r") as f: 
            for linha in f:
                nome,quantidade, preco,categoria = linha.strip().split(";")
                Lista_de_itens.append({
                    "nome": nome,
                    "quantidade": int(quantidade),
                    "preco": float(preco),
                    "categoria":categoria
                })
    except FileNotFoundError:
          print("Arquivo não encontrado, criando novo arquivo.")
    
def registrar_historico(texto): 
    with open("2026-PS/02_mineProjeto/historico.txt", "a", encoding="utf-8" ) as arquivo:
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
                    else:
                        mgs = "Opção invalida"
                print(mgs)
                
            except Exception as e:
                print(f"Erro inesperado {e}")

def Cadastrar_item():
    categoria = verificacao_numerica(opcoes=["CD","Jogos","Livros"],lista_de_opçoes="Escolha a categoria.\n[1]CD\n[2]Livro\n[3]Jogos\n")
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
    estatiticas_do_sistema_lista = {"itens_distintos":0,"total_de_itens":0,"valor_total":0}
    for produto in Lista_de_itens:
        estatiticas_do_sistema_lista["itens_distintos"] += 1
        estatiticas_do_sistema_lista["total_de_itens"] += produto["quantidade"]
        estatiticas_do_sistema_lista["valor_total"] += produto["preco"]*produto["quantidade"]
    print(f"Quantidade de itens diferentes: {estatiticas_do_sistema_lista['itens_distintos']}\nTotal de itens: {estatiticas_do_sistema_lista['total_de_itens']}\nValor total de todos os itens: {estatiticas_do_sistema_lista['valor_total']:.2f}")

def busca():
    while True:
        verificacao = "n"

        print("\n=== BUSCA DE ITENS ===")
        print("[1] Buscar por nome (podendo ser parte do nome, fazendo todos os item com essa parte do nome aparecer).")
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

def menu(): # diz oque o codigo faz
    while True: # loop
        print("\n📋 MENU")
        time.sleep(0.5) # biblioteca time para dar uma pausa entre as prints
        print("1 - Cadastrar item")
        time.sleep(0.5)
        print("2 - Listar itens")
        time.sleep(0.5)
        print("3 - Atualizar quantidade")
        time.sleep(0.5)
        print("4 - Remover item")
        time.sleep(0.5)
        print("5 - Buscar por item")
        time.sleep(0.5)
        print("0 - Sair")
        time.sleep(0.5)
        try:
            opcao = int(input("Escolha uma opção: "))
            time.sleep(0.5)
        except ValueError:
            print("Entrada inválida! Digite um número.")
            time.sleep(0.5)
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