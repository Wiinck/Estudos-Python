def main():
    num = int(input()) # le a entrada do usuario

    for numero in range(num, num + 12): # numeros pares pulam de 2 em 2, por isso "num + 12", para varrer um espaço de até 12 numero e encontrar os 6 impares
        if numero % 2 != 0: # verifica se o numero é impar
            print(numero)

main()
