# Projeto: Prática de Estruturas de Dados em Python (Parte 1)
# Conceitos aplicados: List Comprehensions, Transformação de Strings, 
# Filtragem de dados e Operações matemáticas em listas.


def main():
  estoque = [5, 12, 18, 7, 25, 3, 30]
  estoque_critico = [estoques for estoques in estoque if estoques < 10]

  print(estoque_critico)

main()
