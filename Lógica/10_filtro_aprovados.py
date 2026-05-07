def main():
    notas_turma = [4.5, 7.0, 9.0, 5.8, 10.0, 6.2]
    notas_aprovado = [notas for notas in notas_turma if notas >= 7]

    print(f"As notas que foram aprovadas são: {notas_aprovado}")


main()



