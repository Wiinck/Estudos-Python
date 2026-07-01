def main():
    num = int(input()) #Le o numero digitado e armazena em "num"

    valores = [list(map(float, input().split())) for i in range(num)] # Le os numeros que serao digitados na sequencia de "num", todos sao armazenados na lista "valores[]"

    for nota in valores: # Condicao que percorre cada nota dentro da lista "valores[]"
        nota1 = nota[0] # Acessa o conteudo da lista "valores[]" na posicao 0
        nota2 = nota[1] # Acessa o conteudo da lista "valores[]" na posicao 1
        nota3 = nota[2] # Acessa o conteudo da lista "valores[]" na posicao 2
        
        media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10 # Multiplica cada nota por seu peso, soma tudo e divide pela soma dos pesos (10)

        print(f"{media_ponderada:.1f}") # Imprime a media ponderada das notas 

main()
