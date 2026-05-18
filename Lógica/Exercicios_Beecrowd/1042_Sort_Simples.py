def main():
    numeros = list(map(int, input().split()))
    numeros_crescente = sorted(numeros)
    numeros_decrescente = sorted(numeros, reverse = True)

    for n in numeros_crescente:
        print(n)

    print()

    for n in numeros:
        print(n)


main()
