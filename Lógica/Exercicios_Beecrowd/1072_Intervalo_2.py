def main():
    num = int(input())
    in_intervalo = 0
    out_intervalo = 0

    valores = [int(input()) for i in range(num)]

    for numero in valores:
        if numero in range(10, 20 + 1):
            in_intervalo += 1
        else: 
             out_intervalo += 1

    print(f"{in_intervalo} in")
    print(f"{out_intervalo} out")

main()
