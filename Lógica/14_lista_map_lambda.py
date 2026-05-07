def main():
    alunos = ["manoel", "cleiton", "amanda"]
    alunos_vips = list(map(lambda nome_maiusculo: nome_maiusculo.upper(), alunos))

    print(f"Alunos na lista: {alunos}")
    print(f"Alunos fomatado: {alunos_vips}")
main()
