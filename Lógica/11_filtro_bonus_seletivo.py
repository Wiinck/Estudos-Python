def main():
    notas_turma = [4.5, 7.0, 9.0, 5.8, 10.0, 6.2]
    aprovados_com_bonus = [notas + 0.5 for notas in notas_turma if notas >= 7]

    print(f"As notas foram: {notas_turma}")
    print(f"As notas aprovadas que ganharam bônus: {aprovados_com_bonus}")

main()
