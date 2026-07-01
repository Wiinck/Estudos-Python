def main():
    num = int(input()) # Armazena quantidade de valores que serão lidos em seguida

    valores = [int(input()) for i in range(num)] # Le os valores de entrada no tamanho de "num" e armazena na lista "valores"

    for numero in valores: # Percorre cada numero da lista "valores[]"
        if numero == 0:
            print("NULL")
            
        elif numero % 2 == 0: # Verifica se o numero da lista "valores[]" é um numero par
            if numero > 0: # Verifica se o numero da lista "valores[]" é um numero positivo
                print("EVEN POSITIVE")
            else:
                print("EVEN NEGATIVE")

        elif numero % 2 != 0: # Verifica se o numero da lista "valores[]" é um numero impar
            if numero > 0: # Verifica se o numero da lista "valores[]" é um numero positivo
                print("ODD POSITIVE")
            else:
                print("ODD NEGATIVE")
        
        
main()
