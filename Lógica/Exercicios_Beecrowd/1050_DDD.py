def main():
    A = input()

    telefones_dict = {
        "61": "Brasilia",
        "71": "Salvador",
        "11": "Sao Paulo",
        "21": "Rio de Janeiro",
        "32": "Juiz de Fora",
        "19": "Campinas",
        "27": "Vitoria",
        "31": "Belo Horizonte",
    }

    if A in telefones_dict:
        print(telefones_dict[A])
    else:
        print("DDD nao cadastrado")

main()
