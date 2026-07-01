def main():
    valores = [int(input()) for i in range(1, 100 + 1)] # Le valores de 1 até 100 + 1 (forma de incluir o 100 na condicao) e armazena na lista "valores[]"

    for numero in valores: # Condicao para percorrer todos os valores da lista "valores[]"
        maior = max(valores) # Encontra o maior valor da lista "valores[]"
        posicao = valores.index(maior) # Encontra a posicao do maior numero na lista "valores[]"

    print(maior) # Imprime o maior numero da lista
    print(posicao + 1) # Imprime a posicao do maior valor da lista

main()
