def main():
    usuarios = ["Ana", "Carlos", "Beto", "Alessandra", "Edu"]
    nomes_longos = [nomes for nomes in usuarios if len(nomes) > 5]

    print(f"Nomes com mais de 5 letras: {nomes_longos}")

main()
