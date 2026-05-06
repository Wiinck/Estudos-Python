def main():
  num = int(input("Qual tabuada você quer ver? "))

  for tabuada in range(1, 11):
    resultado = num * tabuada
    print(f"{num} X {tabuada} = {resultado}")

main()
