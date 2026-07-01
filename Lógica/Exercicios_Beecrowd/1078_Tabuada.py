def main():
    num = int(input()) # Le o numero digitado e armazena em "num"

    for numero in range(1, num): # Condicao que percorre todos os numeros de 1 até "num" (numero digitado pelo usuario)
        print(f"{numero} x {num} = {num * numero}") # Imprime a tabuada do numero digitado

main()
