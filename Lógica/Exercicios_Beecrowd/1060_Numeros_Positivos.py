def main():
    valores = [float(input()) for i in range(6)]
    numeros_positivos = 0

    for i in valores:
        if i > 0:
            numeros_positivos += 1

    print(f"{numeros_positivos} valores positivos")
    
main()
