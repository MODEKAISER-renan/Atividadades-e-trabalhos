'''
Nome: Renan Soares da Silva
Matéria: Programação de Sistemas
Professor: Berssa
Data: 28.03.2026
'''

# ============================== CONSTANTES DO SISTEMA ==============================
SEPARADOR = "|"  # Define o caractere separador usado no arquivo

# ============================== ESTRUTURA DE DADOS INICIAL ==============================
catalogo = [
    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt", "disponivel": True},
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "disponivel": False},
    {"titulo": "Padrões de Projeto", "autor": "Erich Gamma", "disponivel": True}
]
# Lista de dicionários: cada item representa um livro com título, autor e status

# ============================== FUNÇÃO: BUSCAR LIVRO ==============================
def buscar_livro(catalogo):
    print("\n--- Buscar Livro ---")
    termo = input("Digite parte do título: ").strip().lower()  # Normaliza entrada do usuário
    try:
        resultados = [l for l in catalogo if termo in l["titulo"].lower()]  # Filtragem condicional
        if not resultados:
            print(" Nenhum livro encontrado.")
            return
        print(f"\n {len(resultados)} resultado(s):")
        for livro in resultados:
            status = "Disponível" if livro["disponivel"] else "Emprestado"
            print(f" • {livro['titulo']} - {livro['autor']} [{status}]")
    except Exception as e:
        print(f" Erro inesperado: {e}")  # Captura erro genérico

# ============================== FUNÇÃO: LISTAR LIVROS ==============================
def listar_livros(catalogo):
    print("\n" + "=" * 50)
    print("CATÁLOGO DA BIBLIOTECA")
    print("=" * 50)
    if not catalogo:
        print("Nenhum livro cadastrado.")
        return
    for i, livro in enumerate(catalogo, 1):  # enumerate começa em 1 para o usuário
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f"{i}. {livro['titulo']} — {livro['autor']}   [{status}]")
    print("=" * 50)

# ============================== FUNÇÃO: ADICIONAR LIVRO ==============================
def adicionar_livro(catalogo):
    print("\n--- Adicionar Novo Livro ---")
    titulo = input("Título: ").strip()
    autor  = input("Autor : ").strip()
    if not titulo or not autor:  # Validação de entrada
        print(" Título e autor são obrigatórios.")
        return
    catalogo.append({
        "titulo": titulo,
        "autor": autor,
        "disponivel": True
    })  # Adiciona novo item ao catálogo
    print(f" '{titulo}' adicionado com sucesso!")

# ============================== FUNÇÃO: REGISTRAR EMPRÉSTIMO ==============================
def registrar_emprestimo(catalogo):
    listar_livros(catalogo)
    if not catalogo:
        return
    print("\n--- Registrar Empréstimo ---")
    try:
        numero = int(input("Número do livro: "))
        if numero < 1 or numero > len(catalogo):  # Validação de intervalo
            print(" Número fora do intervalo.")
            return
        livro = catalogo[numero - 1]  # Ajuste de índice (lista começa em 0)
        if not livro["disponivel"]:
            print(f" '{livro['titulo']}' já está emprestado.")
        else:
            livro["disponivel"] = False  # Atualiza estado
            print(" Empréstimo registrado.")
    except ValueError:
        print(" Entrada inválida. Digite apenas números.")  # Tratamento de erro de tipo

# ============================== FUNÇÃO: DEVOLVER LIVRO ==============================
def devolver_livro(catalogo):
    listar_livros(catalogo)
    if not catalogo:
        return
    print("\n--- Registrar Devolução ---")
    try:
        numero = int(input("Número do livro: "))
        livro = catalogo[numero - 1]
        if livro["disponivel"]:
            print(" Livro já disponível.")
        else:
            livro["disponivel"] = True  # Atualiza estado
            print(" Devolução registrada.")
    except ValueError:
        print(" Digite apenas números.")
    except IndexError:
        print(" Número inválido.")  # Fora do intervalo

# ============================== FUNÇÃO: CARREGAR ARQUIVO ==============================
def carregar_catalogo():
    catalogo = []
    try:
        with open("2026-PS/01_tryFile/biblioteca.txt", "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue  # Ignora linhas vazias
                partes = linha.split(SEPARADOR)
                if len(partes) != 3:
                    continue  # Ignora linhas inválidas
                titulo, autor, disponivel_str = partes
                catalogo.append({
                    "titulo": titulo,
                    "autor": autor,
                    "disponivel": disponivel_str == "True"
                })  # Conversão de string para booleano
    except FileNotFoundError:
        pass  # Arquivo ainda não existe
    return catalogo

# ============================== FUNÇÃO: SALVAR ARQUIVO ==============================
def salvar_catalogo(catalogo):
    try:
        with open("2026-PS/01_tryFile/biblioteca.txt", "w", encoding="utf-8") as f:
            for livro in catalogo:
                linha = f"{livro['titulo']}{SEPARADOR}{livro['autor']}{SEPARADOR}{livro['disponivel']}\n"
                f.write(linha)  # Escrita no arquivo
        print(" Catálogo salvo com sucesso.")
    except IOError as e:
        print(f" Erro ao salvar: {e}")  # Tratamento de erro de escrita

# ============================== MENU PRINCIPAL ==============================
def menu():
    catalogo = carregar_catalogo()  # Carrega dados do arquivo
    print("\n==== SISTEMA DE BIBLIOTECA ====")
    opcoes = {
        "1": ("Listar livros", listar_livros),
        "2": ("Adicionar livro", adicionar_livro),
        "3": ("Buscar livro", buscar_livro),
        "4": ("Registrar empréstimo", registrar_emprestimo),
        "5": ("Devolver livro", devolver_livro),
        "0": ("Sair", None),
    }
    while True:
        print("\nOpções:")
        for chave, (descricao, _) in opcoes.items():
            print(f"[{chave}] {descricao}")  # Exibe menu
        escolha = input("\nSua escolha: ").strip()
        if escolha not in opcoes:
            print(" Opção inválida.")
            continue
        if escolha == "0":
            salvar_catalogo(catalogo)  # Salva antes de sair
            print(" Até logo!")
            break
        _, funcao = opcoes[escolha]
        funcao(catalogo)  # Executa função escolhida

# ============================== EXECUÇÃO DO PROGRAMA ==============================
if __name__ == "__main__":
    menu()  # Ponto de entrada do sistema
