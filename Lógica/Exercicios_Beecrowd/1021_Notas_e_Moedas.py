def main():
    numero = float(input())

    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

    print("NOTAS:")
    for nota in notas:
        cedula = int(numero // nota)
        numero = (numero % nota) + 0.00001
        print(f"{cedula} nota(s) de R$ {nota:.2f}")
    
    print("MOEDAS:")
    for moeda in moedas:
        centavo = int(numero // moeda)
        numero = (numero % moeda) + 0.00001

        print(f"{centavo} moeda(s) de R$ {moeda:.2f}")

main()
