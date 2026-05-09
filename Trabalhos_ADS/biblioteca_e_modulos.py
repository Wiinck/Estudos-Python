import matplotlib.pyplot as plt

# Classe Livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"{self.titulo} por {self.autor}, foi publicado em {self.ano_publicacao}"

# Lista de livros e anos de publicação
biblioteca = []
lista_anos = []

# Função de cadastro de Livros
def cadastro_livros(titulo, autor, ano_publicacao):
    novo_livro = Livro(titulo, autor, ano_publicacao)
    biblioteca.append(novo_livro)
    lista_anos.append(ano_publicacao)
    print(f"O livro {novo_livro} foi adicionado a biblioteca.")

# Função para listar livros
def listar_livros():
    print("Livros na biblioteca:")
    for livro in biblioteca:
        print(livro)

# Função para buscar um livro pelo título
def buscar_livro():
    buscar = input("Digite o nome de um livro: ")
    encontrado = False

    for livro in biblioteca:
        if buscar.lower() == livro.titulo.lower():
            print(livro)
            encontrado = True
            break
    
    if not encontrado:
        print(f"O livro {buscar} não está cadastrado.")

# Função para gerar gráficos
def gerar_grafico():
    # Cria uma lista de anos únicos para o eixo X
    anos_unicos = list(set(lista_anos))
    anos_unicos.sort()

    # Contagem de livros por cada ano único
    contagem_por_ano = [lista_anos.count(a) for a in anos_unicos]

    # Cria um gráfico de linha
    plt.plot(anos_unicos, contagem_por_ano, marker='o', linestyle='-')
    plt.xlabel('Ano de Publicação')
    plt.ylabel('Número de Livros')
    plt.title('Distribuição de Livros na Biblioteca por Ano de Publicação')

    # Adiciona rótulos aos pontos de dados
    for i, valor in enumerate(contagem_por_ano):
        plt.text(anos_unicos[i], valor, str(valor), ha='center', va='bottom')

    plt.grid(True)
    plt.show()

def main():
    dados_novos_livros = [
        ("Harry Potter", "J.K. Rowling", 1997),
        ("Dom Casmurro", "Machado de Assis", 1899),
        ("Código Limpo", "Robert C. Martin", 2008),
        ("O Algoritmo Mestre", "Pedro Domingos", 2015),
        ("1984", "George Orwell", 1949),
        ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943),
        ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954),
        ("O Hobbit", "J.R.R. Tolkien", 1937),
        ("A Metamorfose", "Franz Kafka", 1915),
        ("Sapiens", "Yuval Noah Harari", 2011)
    ]

    # Adiciona os livros e os anos
    for titulo, autor, ano_p in dados_novos_livros:
        novos_livros = Livro(titulo, autor, ano_p)
        biblioteca.append(novos_livros)
        lista_anos.append(ano_p)

    # Chamadas de funções
    print("--- Sistema de Busca de Livros ---")
    buscar_livro()
    gerar_grafico()

main()
