def main():
    num = int(input())

    for numero in range(1, num + 1):
        if numero % 2 == 0:
            quadrado = numero ** 2
            print(f"{numero}^2 = {quadrado}")
main()
