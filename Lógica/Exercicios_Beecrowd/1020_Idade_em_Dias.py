def main ():
    num = int(input())

    tempo = num // 365
    num = num % 365

    meses = num // 30
    dias = num % 30

    print(f"{tempo} ano(s)")
    print(f"{meses} mes(es)")
    print(f"{dias} dia(s)")



main()
