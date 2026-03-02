'''
Código da Maisa
'''
#NOTA IMPORTANTE BERSSA, o código da maisa tem algum detalhe que nã ta funcionando porem o do renan e do felipe esão funcionando
import os #vê se o arquivo usuario.txt já existe no computador.

print("BEM VINDO AO EMPRESTA IFPR!")
print()
print("============================")
print()

arquivo = "usuario.txt"

while True:
    print("\n=== ÍNICIO ===")
    print("1 - Login")
    print("2 - Cadastrar")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    # PRIMEIRO ACESSO automático
    if not os.path.exists(arquivo):
        print("\n=== PRIMEIRO ACESSO ===")
        email = input("Crie seu email: ")
        senha = input("Crie sua senha: ")

    with open(arquivo, "w") as f:
        f.write(email + "\n")
        f.write(senha)

        print("Cadastro realizado com sucesso!")
        continue

    # LOGIN
    if opcao == "1":
        print("\n=== LOGIN ===")
        email_digitado = input("Digite seu email: ")
        senha_digitada = input("Digite sua senha: ")

        with open(arquivo, "r") as f:
            email_salvo = f.readline().strip()
            senha_salva = f.readline().strip()

        if email_digitado == email_salvo and senha_digitada == senha_salva:
            print("Login realizado com sucesso!")
        else:
            print("Email ou senha incorretos.")

    # CADASTRAR NOVAMENTE
    elif opcao == "2":
        email = input("Novo email: ")
        senha = input("Nova senha: ")

        with open(arquivo, "w") as f:
            f.write(email + "\n")
            f.write(senha)

        print("Conta atualizada com sucesso!")

    # SAIR
    elif opcao == "3":
        print("Saindo...")
        break

    else:
     print("Opção inválida.")


'''
Código do Renan
'''
Lista_de_itens = []
verificacao = 1
aux = ''

def titulo(msg):
    print("="*50)
    print(msg)
    print("="*50)
def msgs(msg):
    print(msg)


while verificacao == 1:
    msg = "Sistema para cadastrar materiais"
    titulo(msg)
    msg = "\nO que você deseja cadrastar?"
    msgs(msg)
    Lista_de_itens.append(input("digite o nome do item:").lower())
    msg = "Deseja colocar mais algum item?\nsim[1]\nnão[2]"
    msgs(msg)
    verificacao = int(input())
# código do felipe

solicitacao = input("Solicitação de empréstimo s/n: ")
input("Deseja ver quais itens estão disponiveis para emprestimo? (s/n): ")

if solicitacao == "s":
    print("Os Itens disponíveis para empréstimo são: ")
    for item in Lista_de_itens:
        print(item)
else:
    print("Solicitação de emprestimo cancelada.")

emprestimo = input("Qual item deseja emprestar? ")

if emprestimo in Lista_de_itens:
    print(f"Você solicitou o empréstimo de {emprestimo}.")
else:
    print("O item não esta disponivel.")