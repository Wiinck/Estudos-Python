def main():
    A, B, C, D = map(int, input().split())

    SomaCD = C + D
    SomaAB = A + B

    if B > C and D > A and SomaCD > SomaAB and C > 0 and D > 0 and A % 2 == 0:
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")


main()
