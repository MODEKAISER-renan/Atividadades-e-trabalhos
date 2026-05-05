'''
Arquivo: pet.py
Diciplina: Programação de Sistemas (2026-2)
Aula : Aula 20 - Por que POO
Autor : Renan Soares da Silva
conceitos : classe, objeto, atributos, métodos, encapsulamento
Atividade: Classe Pet
'''

class Pet:
    def __init__(self, nome, especie,idade,telefone_dono,peso,observacoes,vacinado,nome_do_dono):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.nome_do_dono = nome_do_dono
        self.telefone_dono = telefone_dono
        self.peso = peso
        self.vacinado = vacinado
        self.observacoes = observacoes
        self.hospedado = False
    
    def exibir_dados(self):
        print("\n---Dados do Pet ---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Vacinação: {'Sim' if self.vacinado == 's' else 'Não'}")
        print(f"Observações: {self.observacoes}")
        print(f"Telefone do dono: {self.telefone_dono}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")
    
    def registrar_entrada(self):
        if self.hospedado == True:
            print("O pet já está no hotel")
        else:
            self.hospedado = True
            print(f"{self.nome} entrou no hotel")
    
    def calcular_diaria(self):
        if self.idade <= 3:
            return 50.00
        elif self.idade <= 10:
            return 60.00
        else:
            return 75.00
    
    def verificar_vacinacao(self):
        if self.vacinado != 's':
            return "Atenção: vacinação pendente."
        else:
            return "Vacinação em dia."
    
    def atualzar_peso(self, novo_peso):
        self.peso = novo_peso
    
    def emitir_resumo(self):
        msg = f"\nNome do pet: {self.nome}\nEspécie: {self.especie}\nIdade: {self.idade}\nNome do dono: {self.nome_do_dono}\nPeso; {self.peso}\nEstatus de hospedagem: {"está hospedado" if self.hospedado else "não hospedado"}\nSituação de vacina: {self.verificar_vacinacao()}\nValor da diaria: R${self.calcular_diaria()}."
        print(msg)
    
pet1 = Pet("Rex","Cachoro",5,"(+55) 9 2738-0019",15,"nenhuma obseservação","s","Edinaldo Machado pereira")

pet1.exibir_dados()
pet1.registrar_entrada()
pet1.exibir_dados()
pet1.emitir_resumo()





#def __init__(self, nome, especie,idade,telefone_dono,peso,observacoes,vacinado,nome_do_dono):
