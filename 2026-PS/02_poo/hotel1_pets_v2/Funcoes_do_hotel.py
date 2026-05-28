'''
Data: 14.05.2026
Nome: renan Soares da Silva
Obejetivo: Criar um menu para o objeto pets, com objetivo principal do menu de manipular dados do pets, catrasdar e salvar no minimo em txt.
'''

import pickle
import json
import os
from Objetos import *

def salvar_em_json(lista_pets,URL):
    """
    Salva a lista de objetos Pet no arquivo pets.json.
    """

    lista_dicionarios = []

    for pet in lista_pets:
        lista_dicionarios.append(pet.para_dicionario())

    with open(URL, "w", encoding="utf-8") as arquivo:
        json.dump(lista_dicionarios, arquivo, ensure_ascii=False, indent=4)

    print(f"Dados salvos com sucesso em {URL}")

def carregar_pets(URL):
    """
    Carrega os pets do arquivo pets.json.

    Se o arquivo ainda não existir, retorna uma lista vazia.
    """

    if not os.path.exists(URL):
        return []

    with open(URL, "r", encoding="utf-8") as arquivo:
        lista_dicionarios = json.load(arquivo)

    lista_pets = []

    for dados in lista_dicionarios:
        pet = Pet.criar_de_dicionario(dados)
        lista_pets.append(pet)

    return lista_pets

def salvar_em_binario(contatos,URL):
     try:
          with open(URL, "wb") as arquivo:
               pickle.dump(contatos,arquivo)
          print(f"* {len(contatos)} contatos(s) salvos(s) em {URL}")
     except Exception as e:
         print(f"Erro inesperado {e} , arquivo não pode ser salvo")

def carregar_de_binario(URL):
    try:
        with open(URL, "rb") as arquivo:
            Lista = pickle.load(arquivo)
            print(Lista)
            return Lista
    except FileNotFoundError:
        print(f"Arquivos {URL} ainda não existe. Começando vazio")
        return []

def verificacao(funcao,pergunta_principal,auxiliar = "", mgs_auxiliar = ""):
     if funcao == "numerica":
          while True:
               try:
                    numero = int(input(pergunta_principal))
                    return numero
               
               except Exception as e:
                    print(f"Erro inesperado {e}")
                    continue
     elif funcao == "contem?":
          while True:
                    str1 = input(pergunta_principal)
                    if auxiliar in str1:
                         return str1
                    else:
                         print(mgs_auxiliar)