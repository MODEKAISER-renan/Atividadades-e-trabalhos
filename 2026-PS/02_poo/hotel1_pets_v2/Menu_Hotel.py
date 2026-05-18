
import Funcoes_do_hotel
from Objetos import *

lista_de_pets = []
lista_de_donos = []

def menu():
     URl_Donos = "2026-PS/02_poo/hotel1_pets_v2/Lista_de_Donos.bin"
     URL_Pets = "2026-PS/02_poo/hotel1_pets_v2/Lista_de_Pets.bin"
     lista_de_pets = Funcoes_do_hotel.carregar_de_binario(URL_Pets)
     lista_de_donos = Funcoes_do_hotel.carregar_de_binario(URl_Donos)

     while True:
          msg = "\n[1] Cadastar\n[2] listar\n[3] salvar em txt\n[4] salvar em binario\n[5] Check-in/check-out\n[6] atualizar dados do pet\n[7] exlcuir pet\n[8] Buscar pet\n[9] Pets hospedados\n[10] Resumo individual\n[0] Sair\n"
          print(msg)

          resposta = Funcoes_do_hotel.verificacao("numerica","Escolha sua opção: ")
          print("\n")

          if resposta == 0:
               Funcoes_do_hotel.salvar_em_binario(lista_de_donos,URl_Donos)
               Funcoes_do_hotel.salvar_em_binario(lista_de_pets,URL_Pets)
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
               Funcoes_do_hotel.salvar_em_binario(lista_de_donos,URl_Donos)
               Funcoes_do_hotel.salvar_em_binario(lista_de_pets,URL_Pets)
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