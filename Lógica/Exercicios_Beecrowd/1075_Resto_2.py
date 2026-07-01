def main():
    num = int(input()) # Le o numero digitado e armazena em "num"

    for numero in range(1, 10000 + 1): # Condição para percorrer todos os numero entra 1 e 10000, incluindo o 10000
        if numero % num == 2: # Verifica que o resto da divisao de "numero" por "num" tem resto 2
            print(numero) # Imprime todos os numero que tem resto 2 da divisao de "numero" por "num"
        
main()
