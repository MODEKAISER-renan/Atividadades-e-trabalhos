'''
Aluno: Renan Soares da Silva
Data: 03.03.2026
Materia: Porgramação de sistemas
================================
DESCRIÇÂO: fazer um sistema de estoque que ira ler e gaurdar dados de produtos sendo eles na segunite calibração (produto + quantidade), com possibilidade de adicionar itens da lista e contabilizar cada item falando a sua situção sendo critica/ok/mais do que o suficiente,
'''
#VARIAVEIS E LISTAS

#Banco de dados do sistema que ira guradar as informações principais do códgio
Banco_de_dados = [
    {"item":"CPU","quantidade":5},
    {"item":"Memoria RAM","quantidade":11},
    {"item":"Coler","quantidade":2}
]
#Um sub banco de dados especifico para valores numericos sobre dados do sistema como um geral
Banco_Numerico = {
    "quantidade critica":0,
    "quantidade aceitavel":0,
    "Quantidade excessiva":0
}
#local de variaveis sendo a verificação_mae sendo responsavel por deixar o código rodando, sendo a principal
verificacao_mae = "s"
quantidade = 0
item_posição = 0

# FUNÇÕES PRINCIPAIS

#Funções simples puramente esteticas
def msgs(msg):
    print('\n',msg.center(100))
def titulo(msg):
    print("="*100)
    print(msg.center(100))
    print("="*100)

#Faz a verificação e listagem do Banco de dados, ele lista todos os produtos e a situação deles e transforma em numero, e esse número ele armazena no Banco de dados numerico fazendo que seja masi facil de conferir a situação dos itens
def verificacao_do_BancoDeDados():
    global Banco_Numerico
    Banco_Numerico["quantidade aceitavel"] = 0
    Banco_Numerico['quantidade critica']   = 0
    Banco_Numerico['Quantidade excessiva'] = 0
    for produto in Banco_de_dados:
        nome  = produto["item"]
        quant = produto["quantidade"]
        if quant > 10:
            msg = "Ha mais que o suficiente, não é necssario reposição do produto"
            Banco_Numerico["Quantidade excessiva"] += 1
        elif quant >= 5:
            msg = "Ha a quantidade ideal de produto,não ha necessidade de pouca procura mais produto"
            Banco_Numerico["quantidade aceitavel"] += 1
        else:
            msg = "Quantidade crítica, ha necessidade de procurar mais desse produto"
            Banco_Numerico["quantidade critica"] += 1
        msgs(msg = nome)
        msgs(msg = str(quant))
        msgs(msg = msg)

#Atráves da entrada do usuario ele passa por todo banco de dados procurando o item digitado, em cao de erro pede que tente novamente até encontrar o item, caso de sucesso ele ira mostrar a situação, quantidade e nome do item
def busca_de_item():
    item_nome = input("digite o nome do item: ").lower()
    item_encontrado = ''
    for produto in Banco_de_dados:
        if item_nome == produto["item"].lower():
            nome  = produto["item"]
            quant = produto["quantidade"]
            print(f"Item: {nome} Quantidade: {str(quant)}".center(100))
            item_encontrado = "s"
            return
    if item_encontrado != "s":
        print('item não foi encontrado, tente novamente')
        busca_de_item()

#Faz uma verificação para ver se a quantidade do item de entrada é um valo rmaior que zero, caso de erro ele entra em um loop até o usuario digitar um valor numerico valido
#Adendo, na revisão final pedi ao chat ver os erros lógicos e me explicar, aqui eu tava usando o While True: com o códgio já feito, o que torna reduntante e em caso que o usuario erre muitas vezes o sistema pode falhar ou sobre carregar.
def verificacao_se_item_positivo():
    global quantidade
    quantidade = int(input("Digite o valor do item:"))
    if quantidade < 0:
        msgs(msg = "Item invalido, digite novamente: ")
        verificacao_se_item_positivo()
    else:
        return quantidade
# Um adendo, esse código em específico foi feito com ajuda da Xara(ChatGPT que eu treinei para me auxiliar a compreender melhor os códigos e melhora minha lógica de proramação), ele coloca uma nova biblioteca na lista do Banco de dados (inclusive, bem curioso que o = em python é uma ordem e em outas linguagens como C ou java é uma operação)
def adiconar_novo_item():
    Banco_de_dados.append(
        {"item":input("Digite o nome do item: "),"quantidade":quantidade}
    )

#Este código roda todo o código verificando sempre o menor item e após ver todo o banco de dados retorna com a posição do item. (também teve intervesão da Xara, porém eu usei pra entender como pegar um valor especifico em uma lista com varias bibliotecas, no caso primeiro acessa a bliblioteca na possição e depois pode realmente utiliz-la)
def verificacao_item_critico(): # Coreção da Xara, faltou um "i" em "verificacao...", isso pode difultar a leitura de um progamardor na ora de arrumar o código ou de modificar.
    global item_posição
    item_quantidade =  Banco_de_dados[0] #onde usei a Xara
    item_quantidade = item_quantidade["quantidade"] #onde usei a Xara
    for produto in Banco_de_dados:
        if produto["quantidade"] < item_quantidade:
            item_quantidade = produto["quantidade"]
            item_posição = produto
    print("\nItem mais critico do estoque: ",item_posição["item"],item_posição["quantidade"])



#CÓDIGO FUNCIONAL/ CÓDIGO MÃE        

#Aqui realemnete executa todas as funções feitas de forma ordenada criando a interface do usuario    
while verificacao_mae == "s":
    titulo(msg = "Lista dos Itens que Estão no Estoque")
    verificacao_do_BancoDeDados()
    msgs(msg = "vai quere ver a situação de um item em particular? s/n")
    verificacao = input("".center(50))
    if verificacao == "s":
        busca_de_item()
    msgs(msg = "É de seu requerimento adicionar um novo item? s/n")
    verificacao = input("".center(50))
    if verificacao == "s":
        verificacao_se_item_positivo()
        adiconar_novo_item()
    msgs(msg = "Deseja repetir o código? s/n")
    verificacao_mae = input("digite sua resposta:")


# Aqui é a finalização do código, o "rotulo do roda pé", mostradno os dados finasi do sistema e finalizando.
print(f"Quantidade de produtos que tem mais que o suficiente: {Banco_Numerico['Quantidade excessiva']}")
print(f"Quantidade de itens que estão em boa quantidade: {Banco_Numerico['quantidade aceitavel']}")
print(f"Quantidade de itens que estão em estado crítico no estoque: {Banco_Numerico['quantidade critica']}")
verificacao_item_critico()
#Mensagem final.
print("Sistema finalizado")