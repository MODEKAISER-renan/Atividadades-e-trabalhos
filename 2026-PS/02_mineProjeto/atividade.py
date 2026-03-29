'''

Diciplina: Programação de Sistemas

Aula: Aula 12 e 13: Mini-projeto Integrador de Lógica e Paradigma Estruturado - Parte 1 e Parte 2

Integrantes: Renan Soares da Silva, Ana Vitoria Schactae Brandao, João Pedro

Descrição: É um Sistema de armanezamento de dados simples para um pequeno comercio onde ele guarda as informações que recebe em dados.txt e marca o horario de cada ação em historico.txt, esse sistema guardas as infromções  da seguinte forma "Nome,quantidada,preco" e da a disponibilidade de adicionar um valor, modificar ou retirar ele, além de ter um sistema de busca e salvalemto automatico toda vez que o código é finalizado da forma correta (selecionar a opção para sair).

'''
#MÓDULOS:

from datetime import datetime

#VARIAVEIS

Lista_de_produtos = []


#TODAS AS FUNÇÕES

#Parte da ana

#Funções de salvamento

def salvar_dados():
    with open("2026-PS/02_mineProjeto/dados.txt", "w", encoding="utf-8") as f: # dados.txt utiliza o modo "w" para reescrever tudo tudo 
        for p in Lista_de_produtos:
            linha = f"{p['nome']};{p['quantidade']};{p['preco']}\n" # adiciona linha ao local de salvamento
            f.write(linha)

def carregar_dados(): # Função de carregamento
    try:
        with open("2026-PS/02_mineProjeto/dados.txt", "r") as f: 
            for linha in f:
                nome, quantidade, preco = linha.strip().split(";") # separa os parâmetros de linha (nome, quantidade e preço) com ponto e vírgula
                Lista_de_produtos.append({ # Cria a lista de produtos
                    "nome": nome, #com nome
                    "quantidade": int(quantidade), #quantidade
                    "preco": float(preco) #e preço
                })
    except FileNotFoundError:
        print("Arquivo não encontrado, criando novo arquivo.")

def registrar_historico(texto): # Função que registra histórico
    with open("2026-PS/02_mineProjeto/historico.txt", "a", encoding="utf-8" ) as arquivo: #utilizando o modo append para adicionar ao final do arquivo txt histórico
        arquivo.write(f"{datetime.now()} - {texto}\n") # é preenchido a data em que cada operação é efetuada no sistema
        


#parte da ana

#FUNÇÕES BASICAS
#parte do renan

def verificacao_numerica(nome="valor"): # Função de validação de valor
    while True:
        try:
            valor = float(input(f"Digite o {nome}: ")) #Soli
            if valor > 0:
                print(f"{nome} valido.")
                return valor
            else:
                print(f"{nome} invalido, tente novamente")
                continue 
        except:
            print("Valor desconhecido, tente novamente.")
            continue

def Cadastrar_produto(): #Função que cadastra o produto solicitado
    nome = input("Digite o nome do produto: ") #Solicita o nome do produto
    for produto in Lista_de_produtos: #Verifica se o produto já existe na lista
        if nome.lower() in produto["nome"].lower(): #Se o nome do produto já existir, retorna a mensagem de erro
            print("Produto já cadastrado!")
            return
    try:
        quantidade = int(verificacao_numerica(nome="quantidade")) #Faz a validação numérica da quantidade
        preco = verificacao_numerica(nome="preço") #Solicita e valida o preço
    except:
        print("Preço inválido!") #Retorna a mensagem se o preço não for válido
        return
    Lista_de_produtos.append({ #Cria uma lista de produtos
        "nome": nome, #Armazenando nome
        "quantidade": quantidade, #quantidade
        "preco": preco #e preço
    })
    print("Produto cadastrado!") # Conclui o cadastro com uma mensagem de confirmação
    registrar_historico(f"Produto cadastrado: {nome}") # Define o horário em que os produtos foram cadastrados, seguidos do nome

def Listar_Produto(): # Lista os produtos
    for produto in Lista_de_produtos: # Para cada produto na lista
        print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R$ {produto['preco']:.2f}") # Mostra nome, quantidade e preço
    registrar_historico(f"Produtos listados") # Define o horário em que os produtos foram listados
       
def Remover_produto(): # Remove os produtos
    item = input("Digite o nome do produto que quer remover:").lower() # Solicita o nome do produto a ser removido
    for produto in Lista_de_produtos: # Para cada produto na lista
        if item in produto["nome"].lower(): # Se o item estiver em produtos
            Lista_de_produtos.remove(produto) # O produto é removido
            print(f"Produto '{produto['nome']}' removido.") # Mostra o produto que foi removido
            registrar_historico(f"Produto removido: {produto['nome']}") # registra que a remoção foi feita
            break
    else:
        print("Produto não encontrado.") # Se não existir, informar que não foi encontrado
def Atualizar_produto(): # Função que atualiza os produtos
    item = input("Digite o nome do produto que quer atualizar: ").lower() # Solicita o produto a ser atualizado
    for produto in Lista_de_produtos: # Para cada produto na lista
        if item in produto["nome"].lower(): # Se o item estiver em produtos
            escolha1 = input("deseja atualizar a quantidade do produto? (s/n): ").lower() # É poissível atualizar a quantidade
            escolha2 = input("deseja atualizar o preço do produto? (s/n): ").lower() # E o preço
            if escolha1 == "s": # Se "s", atualiza a quantidade
                nova_quantidade = int(verificacao_numerica(nome="quantidade"))
                produto["quantidade"] = nova_quantidade
            if escolha2 == "s": # Se "s", atualiza o preço
                novo_preco = verificacao_numerica(nome="preço") 
                produto["preco"] = novo_preco
            print(f"Produto '{produto['nome']}' atualizado.")
            registrar_historico(f"Produto atualizado: {produto['nome']}") # Registra a hora de atualização do preço
            break
    else:
        print("Valor não encontrado.") # Se o item não existir na lista, impede de atualizar preço e quantidade
    
#FUNÇÕES AVANÇADAS 

#função de estatisticas dos dados

def estatiticas_do_sistema(): #Obejetivo: fazer a analize de quantos itens distintos, itens no total e o valor de todos os item gardados em dados.txt
    estatiticas_do_sistema_lista = {"itens_distintos":0,"total_de_itens":0,"valor_total":0}
    for produto in Lista_de_produtos:
        estatiticas_do_sistema_lista["itens_distintos"] += 1
        estatiticas_do_sistema_lista["total_de_itens"] += produto["quantidade"]
        estatiticas_do_sistema_lista["valor_total"] += produto["preco"]*produto["quantidade"]
    print(f"Quantidade de itens diferentes: {estatiticas_do_sistema_lista['itens_distintos']}\nTotal de itens: {estatiticas_do_sistema_lista['total_de_itens']}\nValor total de todos os itens: {estatiticas_do_sistema_lista['valor_total']:.2f}")
    
#função de busca por camadas

def busca():
    #Variaveis locais
    verificacao = "n"

    print("=== BUSCA DE ITENS ===")
    print("[1] Buscar por nome (podendo ser parte do nome, fazendo todos os item com essa parte do nome aparecer).")
    print("[2] Buscar por quantidade de itens.")
    print("[3] Buscar por valor aproximado.")
    resposta = input("Qual opção deseja escolher? ")
    if resposta == "1":
        nome = input("Escreva o nome do produto: ").lower()
        for produto in Lista_de_produtos:
            if nome in produto['nome'].lower():
                verificacao = "s"
                print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R$ {produto['preco']:.2f}")

    elif resposta == "2":
        quantidade = int(verificacao_numerica(nome="Item da busca"))
        for produto in Lista_de_produtos:
            if quantidade == produto['quantidade']:
                verificacao = "s"
                print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R$ {produto['preco']:.2f}")

    elif resposta == "3":
        valor = verificacao_numerica(nome="Valor do item")
        for produto in Lista_de_produtos:
            if valor  >= produto['preco'] - 10 and valor <= produto['preco'] + 10:
                verificacao = "s"
                print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R$ {produto['preco']:.2f}")
    if verificacao == "n":
        print("Item não encontrado")
        registrar_historico("Busca sem resultado")
    else:
        print("\nBusca feita com sucesso!")
        registrar_historico("Busca realizada")


#Função do menu/Função Primordial.

def menu(): # Função que armazena o menu do sistema
    while True:
        print("\n📋 MENU") #Apresenta o menu com as opções numeradas:
        print("1 - Cadastrar produto") #Cadastrar produtos 
        print("2 - Listar produtos") #Listar produtos
        print("3 - Atualizar quantidade") #Atualizar quantidade
        print("4 - Remover produto") #Remover produto
        print("5 - Buscar por item")
        print("0 - Sair") #Sair do programa

        try:
            opcao = int(input("Escolha uma opção: ")) # Solicita a escolha de opção
        except ValueError:
            print("Entrada inválida! Digite um número.") # Se opção inválida, pede para repetir a operação
            continue # Avança se entrada válida

        if opcao == 1: # Se usuário solicitar cadástro de produtos:
            Cadastrar_produto()
        elif opcao == 2:
            Listar_Produto()
        elif opcao == 3:
            Atualizar_produto()
        elif opcao == 4:
            Remover_produto()
        elif opcao == 5:
            busca()
        elif opcao == 0:
            print("Saindo do sistema...")
            salvar_dados() # Salva os dados antes de sair
            estatiticas_do_sistema() # mostrar o relatorio antes de sair do sistema
            break
        else:
            print("Opção inválida!")

#PROGRAMA FUNCINAL AQUI (execução real do código)

if __name__ == "__main__": # Inicia o programa
    carregar_dados() # leitura ao iniciar
    menu()