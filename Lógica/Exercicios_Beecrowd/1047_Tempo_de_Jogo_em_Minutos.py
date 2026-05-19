def main():
    hora_inicial, min_inicial, hora_final, min_final = map(int, input().split())
    
    minutos_inicio = (hora_inicial * 60) + min_inicial
    minutos_fim = (hora_final * 60) + min_final

    diferenca = minutos_fim - minutos_inicio

    if diferenca <= 0:
        diferenca += 24 * 60 

    duracao_hora = diferenca // 60  
    duracao_min = diferenca % 60   

    print(f"O JOGO DUROU {duracao_hora} HORA(S) E {duracao_min} MINUTO(S)")

main()
