'''
Aluno: Renan Soares da Silva
Data: 03.03.2026
Materia: Porgramação de sistemas
================================
DESCRIÇÂO: fazer um sistema de estoque que ira ler e gaurdar dados de produtos sendo eles na segunite calibração (produto + quantidade), com possibilidade de adicionar itens da lista e contabilizar cada item falando a sua situção sendo critica/ok/mais do que o suficiente,
'''
Banco_de_dados = [
    {"item":"CPU","quantidade":5},
    {"item":"Memoria RAM","quantidade":11},
    {"item":"Coler","quantidade":2}
]
Banco_Numerico = {
    "quantidade critica":0,
    "quantidade aceitavel":0,
    "Quantidade excessiva":0
}
verificacao_mae = "s"

def msgs(msg):
    print('\n',msg.center(100))
def titulo(msg):
    print("="*100)
    print(msg.center(100))
    print("="*100)


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
        print(Banco_Numerico)

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




        
    
while verificacao_mae == "s":
    titulo(msg = "Lista dos Itens que Estão no Estoque")
    verificacao_do_BancoDeDados()
    msgs(msg = "vai quere ver a situação de um item em particular? s/n")
    verificacao = input("".center(50))
    if verificacao == "s":
        busca_de_item()

    
print(f"Quantidade de produtos que tem mais que o suficiente: {Banco_Numerico['Quantidade excessiva']}")
print(f"Quantidade de itens que estão em boa quantidade: {Banco_Numerico['quantidade aceitavel']}")
print(f"Quantidade de itens que estão em estado crítico no estoque: {Banco_Numerico['quantidade critica']}")
