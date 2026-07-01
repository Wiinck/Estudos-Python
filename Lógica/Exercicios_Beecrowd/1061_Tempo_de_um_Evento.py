def main():
    dia_inicio = int(input().split()[1]) # Pega só o número depois da palavra "Dia"
    horario_inicio = input()
    dia_fim = int(input().split()[1]) # Pega só o número depois da palavra "Dia"
    horario_fim = input()

    h_inicio, m_inicio, s_inicio = map(int, horario_inicio.split(" : "))
    h_fim, m_fim, s_fim = map(int, horario_fim.split(" : "))


    segundos_inicio = (dia_inicio * 86400) + (h_inicio * 3600) + (m_inicio * 60) + s_inicio
    segundos_fim = (dia_fim * 86400) + (h_fim * 3600) + (m_fim * 60) + s_fim

    segundos_total = segundos_fim - segundos_inicio

    dias = segundos_total // 86400
    resto = segundos_total % 86400

    horas = resto // 3600
    resto = resto % 3600

    minutos = resto // 60
    segundos = resto % 60

    print(f"{dias} dia(s)")
    print(f"{horas} hora(s)")
    print(f"{minutos} minuto(s)") 
    print(f"{segundos} segundo(s)")
    
main()
