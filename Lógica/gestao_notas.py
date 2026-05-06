def main():
  list_notas = []
  media = float()
  notas = float()
  total = float()

  while True:
    notas = float(input("Digite uma nota! (Para sair digite 00): "))
    if notas == 00:
      print("\nOperação cancelada!\n")
      print(f"A média das notas é: {media:.2f}")

      if media >= 7:
        print("Parabéns, você foi Aprovado!")
      else:
        print("Infelizmente você foi Reprovado!")

      print("As notas digitadas foram: ")
      for nota in list_notas:
        print(nota)
      break

    if notas >= 0 or notas <= 10:
      list_notas.append(notas)
                        
      total = sum(list_notas)
      media = total / len(list_notas)

main()
