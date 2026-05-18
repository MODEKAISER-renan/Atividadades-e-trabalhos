'''
Data: 14.05.2026
Nome: renan Soares da Silva
Obejetivo: Criar um menu para o objeto pets, com objetivo principal do menu de manipular dados do pets, catrasdar e salvar no minimo em txt.
'''

import pickle
from Menu_Hotel import menu

URl_Donos = "2026-PS/02_poo/hotel1_pets_v2/Lista_de_Donos.bin"
URL_Pets = "2026-PS/02_poo/hotel1_pets_v2/Lista_de_Pets.bin"

# def salvar_em_txt(, caminho):
#     with open(caminho,"w", encoding="utf-8") as arquivo:
#         for c in contatos:
#             arquivo.write(c.para_linha_txt()+"\n")
#     print(f"* {len(contatos)} contatos(s) salvos(s) em {caminho}")

# def carregar_de_txt(caminho):
#     contatos = []
#     try:
#         with open(caminho,"r",encoding="utf-8") as arquivo:
#             for linha in arquivo:
#                 linha = linha.strip()
#                 if not linha:
#                     continue
#                 partes = linha.strip(";")
#                 nome,telefone,email = partes[0],partes[1],partes[2]
#                 contatos.append(Contato(nome,telefone,email))
#     except FileExistsError:
#         print(f"Arquivo {caminho} ainda não existe. Começando vazio.")
#     return contatos

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