'''
Data: 14.05.2026
Nome: renan Soares da Silva
Obejetivo: Criar um menu para o objeto pets, com objetivo principal do menu de manipular dados do pets, catrasdar e salvar no minimo em txt.
'''

from pet import Pet
import pickle

lista_de_pets = []
lista_de_donos = []

class Dono:
     def __init__(self):
          print("\n=== Cadastro do Dono ===\n")
          self.Nome_Dono = input("Digite Nome do dono: ")
          self.Numero_Dono = verificacao("numerica","Digite seu numero:")
          self.Gmail_Dono = verificacao("contem?","Digite seu Email: ","@","Email invalido, digite novamente")
          print("Cadastro realizado com sucesso.")
    
     def Exibir(self):
          msg =f"\nNome do dono: {self.Nome_Dono}\nNumero do dono: {self.Numero_Dono}\nEmail do dono: {self.Gmail_Dono}\n"
          return msg

     def linha_txt():
          pass

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
            return pickle.load(arquivo)
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

def menu():
     URl_Donos = "2026-PS/02_poo/hotel1_pets_v2/Lista_de_Donos.bin"
     URL_Pets = "2026-PS/02_poo/hotel1_pets_v2/Lista_de_Pets.bin"
     lista_de_pets = carregar_de_binario(URL_Pets)
     lista_de_donos = carregar_de_binario(URl_Donos)

     while True:
          msg = "\n[1] Cadastar\n[2] listar\n[3] salvar em txt\n[4] salvar em binario\n[5] Check-in/check-out\n[6] atualizar dados do pet\n[7] exlcuir pet\n[8] Buscar pet\n[9] Pets hospedados\n[10] Resumo individual\n[0] Sair\n"
          print(msg)

          resposta = verificacao("numerica","Escolha sua opção: ")
          print("\n")

          if resposta == 0:
               salvar_em_binario(lista_de_donos,URl_Donos)
               salvar_em_binario(lista_de_pets,URL_Pets)
               break
          elif resposta == 1:
               usuario = Dono()
               pet = Pet()
               lista_de_donos.append(usuario)
               lista_de_pets.append(pet)
          elif resposta == 2:
               print("\n=== Lsita de donos ===\n")
               for dono in lista_de_donos:
                    print(dono.Exibir())
               print("\n=== Lista de Pets ===\n")
               for pet in lista_de_pets:
                    print(pet.exibir_dados())
          elif resposta == 3:
               pass
          elif resposta == 4:
               salvar_em_binario(lista_de_donos,URl_Donos)
               salvar_em_binario(lista_de_pets,URL_Pets)
          elif resposta == 5:
               print("Digite o nome do pet que deseja fazer check-in: ")
          elif resposta == 6:
               pass
          elif resposta == 7:
               pass
          elif resposta == 8:
               pass
          elif resposta == 9:
               pass
          elif resposta == 10:
               pass


if __name__ == "__main__":
    menu()