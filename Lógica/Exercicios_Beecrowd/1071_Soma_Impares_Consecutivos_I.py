def main():
    num1 = int(input()) # Le o primeiro valor digitado
    num2 = int(input()) # Le o segundo valor digitado
    impares = [] # Lista vazia

    menor = min(num1, num2) # Descobre qual o MENOR valor digitado na entrada
    maior = max(num1, num2) # Descobre qual o MAIOR valor digitado na entrada

    for numero in range(menor + 1, maior): # Em um raio do numero menor (sem contar ele) até o numero maior, descobre quais são os numero impares
        if numero % 2 != 0:
            impares.append(numero)  # adiciona os numeros impares na lisa "impares"

    print(sum(impares)) # Imprime a soma dos numeros que estão na lista "impares"

main()
