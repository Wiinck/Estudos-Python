def main():
    num = int(input())
    notas = [100, 50, 20, 10, 5, 2, 1]

    print(num)
    for nota in notas:
        qtd_notas = num // nota
        num = num % nota
        print(f"{qtd_notas} nota(s) de R$ {nota},00")


main()
