def main():
    valores = [float(input()) for i in range(6)]
    num_posit_lista = []

    for numero in valores:
        if numero > 0:
            num_posit_lista.append(numero)
    
    media = sum(num_posit_lista) / len(num_posit_lista)
    
    print(f"{len(num_posit_lista)} valores positivos")
    print(f"{media:.1f}")

main()
