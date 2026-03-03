'''
Aluno: Renan Soares da Silva
Data: 03.03.2026
Materia: Porgramação de sistemas
================================
DESCRIÇÂO: fazer um sistema de estoque que ira ler e gaurdar dados de produtos sendo eles na segunite calibração (produto + quantidade), com possibilidade de adicionar itens da lista e contabilizar cada item falando a sua situção sendo critica/ok/mais do que o suficiente,
'''
Banco_de_dados = [
    {"item":"CPU","quantidade":5},
    {"item":"memoria ram","quantidade":11},
    {"item":"coler","quantidade":2}
]
Banco_Numerico = {
    "quantidade critica":0,
    "quantidade aceitavel":0,
    "Quantidade excessiva":0
}

def msgs(msg):
    print('\n',msg.center(100))
def titulo(msg):
    print("="*100)
    print(msg.center(100))
    print("="*100)


def verificacao_do_BancoDeDados():
    global Banco_Numerico
    Banco_Numerico["quantidade aceitavel"] = 0
    Banco_Numerico['quantidade critica'] = 0
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
        
    
while True:
    titulo(msg = "Lista dos Itens que Estão no Estoque")
    verificacao_do_BancoDeDados()
    break
