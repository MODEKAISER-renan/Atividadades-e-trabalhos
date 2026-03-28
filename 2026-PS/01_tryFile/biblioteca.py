'''
Nome: renan soares da silva
materia: programação de sistemas
professor: Berssa
data: 28.03.2026
'''

ARQUIVO   = "biblioteca.txt"
SEPARADOR = "|"  

catalogo = [
    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt", "disponivel": True},
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "disponivel": False},
    {"titulo": "Padrões de Projeto", "autor": "Erich Gamma", "disponivel": True}
]

def buscar_livro(catalogo):
    print("\n--- Buscar Livro ---")
    termo = input("Digite parte do título: ").strip().lower()
    try:
        resultados = [l for l in catalogo if termo in l["titulo"].lower()]
        if not resultados:
            print(" Nenhum livro encontrado.")
            return
        print(f"\n {len(resultados)} resultado(s):")
        for livro in resultados:
            status = "Disponível" if livro["disponivel"] else "Emprestado"
            print(f" • {livro['titulo']} - {livro['autor']} [{status}]")
    except Exception as e:
        print(f" Erro inesperado: {e}")


def listar_livros(catalogo):
    print("\n" + "=" * 50)
    print("CATÁLOGO DA BIBLIOTECA")
    print("=" * 50)
    if not catalogo:
        print("Nenhum livro cadastrado.")
        return
    for i, livro in enumerate(catalogo, 1):
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f"{i}. {livro['titulo']} — {livro['autor']}   [{status}]")
    print("=" * 50)

def adicionar_livro(catalogo):
    print("\n--- Adicionar Novo Livro ---")
    titulo = input("Título: ").strip()
    autor  = input("Autor : ").strip()
    if not titulo or not autor:
        print("  Título e autor são obrigatórios.")
        return
    catalogo.append({
        "titulo": titulo,
        "autor": autor,
        "disponivel": True
    })
    print(f" '{titulo}' adicionado com sucesso!")

def registrar_emprestimo(catalogo):
    listar_livros(catalogo)
    if not catalogo:
        return
    print("\n--- Registrar Empréstimo ---")
    try:
        numero = int(input("Número do livro: "))  # ValueError se digitar letras
        if numero < 1 or numero > len(catalogo):
            print("  Número fora do intervalo.")
            return
        livro = catalogo[numero - 1]  # -1 porque lista começa em 0
        if not livro["disponivel"]:
            print(f"  '{livro['titulo']}' já está emprestado.")
        else:
            livro["disponivel"] = False
            print(f" Empréstimo de '{livro['titulo']}' registrado.")
    except ValueError:
        print("  Entrada inválida. Digite apenas o número.")


def devolver_livro(catalogo):
    listar_livros()
    if not catalogo:
        return
    print("\n--- Registrar Devolução ---")
    try:
        numero = int(input("Número do livro a devolver: "))
        livro = catalogo[numero - 1]  
        if livro["disponivel"]:
            print(f"  '{livro['titulo']}' já está disponível.")
        else:
            livro["disponivel"] = True
            print(f"  Devolução de '{livro['titulo']}' registrada.")
    except ValueError:
        print("  Digite apenas o número do livro.")
    except IndexError:
        print("  Número fora da lista. Verifique os livros cadastrados.")

def carregar_catalogo():
    """Lê o .txt e reconstrói a lista de dicionários."""
    catalogo = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:         
                    continue
                partes = linha.split(SEPARADOR)
                if len(partes) != 3:     
                    continue
                titulo, autor, disponivel_str = partes
                catalogo.append({
                    "titulo":     titulo,
                    "autor":      autor,
                    "disponivel": disponivel_str == "True"
                })
    except FileNotFoundError:
        pass
    return catalogo


def salvar_catalogo(catalogo):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            for livro in catalogo:
                linha = f"{livro['titulo']}{SEPARADOR}{livro['autor']}{SEPARADOR}{livro['disponivel']}\n"
                f.write(linha)
        print(f" Catálogo salvo em '{ARQUIVO}'.")
    except IOError as e:
        print(f" Erro ao salvar: {e}")


def menu():
    catalogo = carregar_catalogo()
    total = len(catalogo)
    print(f"\n====SISTEMA DE BIBLIOTECA====")
    print(f"{total} livro(s) carregado(s) de '{ARQUIVO}'.")

    opcoes = {
        "1": ("Listar livros",        listar_livros),
        "2": ("Adicionar livro",      adicionar_livro),
        "3": ("Buscar livro",         buscar_livro),
        "4": ("Registrar empréstimo", registrar_emprestimo),
        "5": ("Devolver livro",       devolver_livro),
        "0": ("Sair",                 None),
    }

    while True:
        print("\nOpções:")
        for chave, (descricao, _) in opcoes.items():
            print(f"    [{chave}] {descricao}")
        try:
            escolha = input("\n  Sua escolha: ").strip()
            if escolha not in opcoes:
                raise ValueError(f"Opção '{escolha}' inválida.")
        except ValueError as e:
            print(f"  {e}")
            continue
        else:
            if escolha == "0":
                print("\n  Até logo! ")
                salvar_catalogo(catalogo)
                break
            
            _, funcao = opcoes[escolha]
            funcao(catalogo)
        finally:
            pass

if __name__ == "__main__":
    menu()              

