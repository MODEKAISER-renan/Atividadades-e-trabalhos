'''
Arquivo: pet.py
Diciplina: Programação de Sistemas (2026-2)
Aula : Aula 20 - Por que POO
Autor : Renan Soares da Silva
conceitos : classe, objeto, atributos, métodos, encapsulamento
Atividade: Classe Pet
'''

import random
from Funcoes_do_hotel import *

class Dono:
    def __init__(self):
        print("\n=== Cadastro do Dono ===\n")
        self.Nome_Dono = input("Digite Nome do dono: ")
        self.Numero_Dono = verificacao("numerica","Digite seu numero:")
        self.Gmail_Dono = verificacao("contem?","Digite seu Email: ","@","Email invalido, digite novamente")
        print("Cadastro realizado com sucesso.")
        ID = random.randint(1,10)
        print(ID)
    
    
    def Exibir(self):
        msg =f"\nNome do dono: {self.Nome_Dono}\nNumero do dono: {self.Numero_Dono}\nEmail do dono: {self.Gmail_Dono}\n"
        return msg

    def para_dicionario(self):
        """
        Transforma o objeto Pet em um dicionário.

        Isso é necessário porque o JSON não salva diretamente objetos Python.
        Ele salva dados simples: textos, números, booleanos, listas e dicionários.
        """
        return {
            "nome": self.Nome_Dono,
            "numero": self.Numero_Dono,
            "email": self.Gmail_Dono,
        }

    @staticmethod
    def criar_de_dicionario(dados):
        """
        Cria um objeto Pet a partir de um dicionário carregado do JSON.
        """
        return Pet(
            dados["nome"],
            dados["numero"],
            dados["email"],
        )


class Pet:
    def __init__(self):
        print("\n=== Cadastro Do Pet ===\n")
        self.nome = input("Digite o nome do pet: ")
        self.especie = input("Digite a especie: ")
        self.idade = int(input("Digite a idade: "))
        self.peso = float(input("Digite o peso: "))
        self.vacinado = input("É vacinado?[s/n]: ")
        self.observacoes = input("Digite se há alguma observação sobre o pet: ")
        self.hospedado = False

    
    def exibir_dados(self):
        print(f"\n---Dados do {self.nome} ---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Vacinação: {'Sim' if self.vacinado == 's' else 'Não'}")
        print(f"Observações: {self.observacoes}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")

    def para_dicionario(self):
        """
        Transforma o objeto Pet em um dicionário.

        Isso é necessário porque o JSON não salva diretamente objetos Python.
        Ele salva dados simples: textos, números, booleanos, listas e dicionários.
        """
        return {
            "nome": self.nome,
            "especie": self.especie,
            "idade": self.idade,
            "peso": self.peso,
            "vacinado": self.vacinado,
            "observacoes":self.observacoes,
            "hospedado": self.hospedado
        }

    @staticmethod
    def criar_de_dicionario(dados):
        """
        Cria um objeto Pet a partir de um dicionário carregado do JSON.
        """
        return Pet(
            dados["nome"],
            dados["especie"],
            dados["idade"],
            dados["peso"],
            dados["vacinado"],
            dados["hospedado"],
            dados["observacoes"]
        )

    
    def registrar_entrada(self):
        print("Deseja fazer:\n[1] check-in\n[2] check-out")
        escolha = input("Digite sua escolha: ")
        if escolha == "1":
            if self.hospedado == True:
                print("O pet já está no hotel")
            else:
                self.hospedado = True
                print(f"{self.nome} está ospedado")
        else:
            if self.hospedado == False:
                print("O pet ainda não está ospedado para fazer check-out")
            else:
                self.hospedado = False
                print(f"{self.nome} fez check-out")
    
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
        msg = f"\nNome do pet: {self.nome}\nEspécie: {self.especie}\nIdade: {self.idade}\nPeso; {self.peso}\nEstatus de hospedagem: {"está hospedado" if self.hospedado else "não hospedado"}\nSituação de vacina: {self.verificar_vacinacao()}\nValor da diaria: R${self.calcular_diaria()}."
        print(msg)
