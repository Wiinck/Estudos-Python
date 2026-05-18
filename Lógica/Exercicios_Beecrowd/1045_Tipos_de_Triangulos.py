def main():
    numeros = map(float, input().split())
    numeros_ordenado = sorted(numeros, reverse=True)
    
    A = numeros_ordenado[0]
    B = numeros_ordenado[1]
    C = numeros_ordenado[2]
    

    if A >=  (B + C):
        print("NAO FORMA TRIANGULO")

    elif (A ** 2) == ((B ** 2) + (C ** 2)):
        print("TRIANGULO RETANGULO")

    elif (A ** 2) > ((B ** 2) + (C ** 2)):
        print("TRIANGULO OBTUSANGULO")

    elif (A ** 2) < ((B ** 2) + (C ** 2)):
        print("TRIANGULO ACUTANGULO")

    if A == B == C: 
        print("TRIANGULO EQUILATERO")

    elif A == B or B == C or C == A:
        print("TRIANGULO ISOSCELES")

main()
