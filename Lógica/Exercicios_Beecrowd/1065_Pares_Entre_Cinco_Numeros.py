def main():
    valores = [int(input()) for i in range(5)]
    numeros_pares = 0

    for numero in valores:
        if numero % 2 == 0:
            numeros_pares += 1

    print(f"{numeros_pares} valores pares")

main()
