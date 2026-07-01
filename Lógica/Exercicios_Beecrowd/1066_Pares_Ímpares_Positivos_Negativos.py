def main():
    valores = [int(input()) for i in range(5)] # Lendo as entradas e armazenando em lista "valores"
    pares = 0
    positivos = 0

    # Laço de repetição para encontrar numeros positivos e numeros pares na lista "valores"
    for numero in valores:
        if numero % 2 == 0:
            pares += 1
        
        if numero > 0:
            positivos += 1
            
    impar = len(valores) - pares
    negativos = len(valores) - positivos - valores.count(0) # Calculando quantos negativos tem na lista. COUNT(0) serve para contar quantos numeros 0 tem na lista e subtrair, já que zero é um numero neutro

    print(f"{pares} valor(es) par(es)")
    print(f"{impar} valor(es) impar(es)")
    print(f"{positivos} valor(es) positivo(s)")
    print(f"{negativos} valor(es) negativo(s)")

main()
