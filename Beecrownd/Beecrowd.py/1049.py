#data: 14.04.2026
#data final: 22.04.2026

lista_de_definicao = [
    {"tipo1":"vertebrado","tipo2":"ave", "tipo3":"carnivoro","individuo1":"aguia"},
    {"tipo1":"vertebrado","tipo2":"ave","tipo3":"onivoro","individuo1":"pomba"},
    {"tipo1":"vertebrado","tipo2":"mamifero","tipo3":"onivoro","individuo1":"homem"},
    {"tipo1":"vertebrado","tipo2":"mamifero","tipo3":"herbivoro","individuo1":"vaca"},
    {"tipo1":"invertebrado","tipo2":"inseto","tipo3":"hematofago","individuo1":"pulga"},
    {"tipo1":"invertebrado","tipo2":"inseto","tipo3":"herbivoro","individuo1":"lagarta"},
    {"tipo1":"invertebrado","tipo2":"anelideo","tipo3":"hematofago","individuo1":"sanguessuga"},
    {"tipo1":"invertebrado","tipo2":"anelideo","tipo3":"onivoro","individuo1":"minhoca"}]

categoria1 = input()
categoria2 = input()
categoria3 = input()

for opcao in lista_de_definicao:
    if opcao['tipo1'] == categoria1 and opcao['tipo2'] == categoria2 and opcao['tipo3'] == categoria3:
        print(opcao['individuo1'])
    