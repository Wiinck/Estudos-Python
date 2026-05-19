def main():
    inicio, fim = map(int, input().split())

    if inicio == fim:
        print("O JOGO DUROU 24 HORA(S)")
    
    elif inicio > fim:
        duracao = (24 - inicio) + fim
        print(f"O JOGO DUROU {duracao} HORA(S)")
    
    elif inicio < fim:
        duracao = fim - inicio
        print(f"O JOGO DUROU {duracao} HORA(S)")


    
main() 
