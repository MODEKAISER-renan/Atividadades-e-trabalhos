
from Funcoes_do_hotel import *
from Objetos import *

lista_de_pets = []
lista_de_donos = []

def menu():
     URl_Donos = "2026-PS/02_poo/hotel1_pets_v2/Lista_de_Donos.bin"
     URL_Pets = "2026-PS/02_poo/hotel1_pets_v2/Lista_de_Pets.bin"
     URl_Donos_json = "2026-PS/02_poo/hotel1_pets_v2/donos.json"
     URL_Pets_json = "2026-PS/02_poo/hotel1_pets_v2/pets.json"
     lista_de_pets = carregar_de_binario(URL_Pets)
     lista_de_donos = carregar_de_binario(URl_Donos)

     while True:
          msg = "\n[1] Cadastar\n[2] listar\n[3] salvar em txt\n[4] salvar em binario\n[5] Check-in/check-out\n[6] atualizar dados do pet\n[7] exlcuir usuario\n[8] Buscar pet\n[9] Pets hospedados\n[10] Resumo individual\n[0] Sair\n"
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
               salvar_em_json(lista_de_pets,URL_Pets_json)
               salvar_em_json(lista_de_donos,URl_Donos_json)
          elif resposta == 4:
               salvar_em_binario(lista_de_donos,URl_Donos)
               salvar_em_binario(lista_de_pets,URL_Pets)
          elif resposta == 5:
               print("Digite o nome do pet que deseja fazer check-in: ")
               nome = input()
               for pet in lista_de_pets:
                    if nome in pet.nome:
                         pet.registrar_entrada()
                    else:
                         print("Nome invalido.")
          elif resposta == 6:
               print("Qual pet deseja alterar os atributos:")
               nome = input("Digite o nome do pet aqui: ")
               busca_erro = True
               for pet in lista_de_pets:
                    if nome in pet.nome:
                         busca_erro = False
                         print("Deseja [1] Atualizar todos os dados do pet [2] Atualizar apeans um ")
                         escolha = verificacao("numerica","digite sua escolha: ")
                         if escolha == 1:
                              pet.nome = input("Digite o novo nome:")
                              pet.idade = int(input("Digite o nova idade: "))
                              pet.peso = float(input("Digite o novo peso: "))
                              pet.vacinado = input("Digite o novo vacinado: ")
                              pet.observacao = input("Digite o nova observação: ")
                         elif escolha == 2:
                              print("Qual dos atributos deseja alterar?\n[1] Nome\n[2] Idade\n[3] Peso\n[4]Vacinado\n[5] Observação")
                              escolha = verificacao("numerica","digite sua escolha: ")
                              if escolha == 1:
                                   pet.nome = input("Digite o novo atributo: ")
                              if escolha == 2:
                                   pet.idade = int(input("Digite o novo atributo: "))
                              if escolha == 3:
                                   pet.peso = float(input("Digite o novo atributo: "))
                              if escolha == 4:
                                   pet.vacinado = input("Digite o novo atributo: ")
                              if escolha == 5:
                                   pet.observacao = input("Digite o novo atributo: ")
                         else:
                              print("Opção invalida")
               if busca_erro != False:
                    print("Opção invaldia")
          elif resposta == 7:
               print("Deseja apagar um dono ou um pet: [1]Dono\n[2]Pet")
               escolha = verificacao("numerica","digite sua escolha: ")
               if escolha == 1:
                    print("Digite o nome do Dono que deseja apagar: ")
                    dono = input("")
                    print(f"realmente deseja apagar {dono} ? s/n")
                    escolha = input().lower()
                    if escolha == "s":
                         for usuario in lista_de_donos:
                              if dono == usuario:
                                   lista_de_donos.remove(usuario)
                    else:
                         print("Opção de detelar cancelada ou opção invalida")
                         pass

               elif escolha == 2:
                    print("Digite o nome do Pet que deseja apagar: ")
                    pet = input("")
                    print(f"realmente deseja apagar {pet} ? s/n")
                    escolha = input().lower()
                    if escolha == "s":
                         for usuario in lista_de_donos:
                              if pet == usuario:
                                   lista_de_pets.remove(usuario)
                    else:
                         print("Opção de detelar cancelada ou opção invalida")
                         pass
               else:
                    print("Opção invalida")
          elif resposta == 8:
               pass
          elif resposta == 9:
               pass
          elif resposta == 10:
               pass


if __name__ == "__main__":
    menu()