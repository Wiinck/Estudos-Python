def main():
  saldo = 500

  while saldo > 0:
    num = float(input("Digite um valor para sacar: "))

    if num == 0:
      print("Operação cancelada. Saindo...")
      break

    if num <= saldo:
      saldo -= num
      print(f"Saque realizado! Saldo atual: R$ {saldo:.2f}")
      continue

    if num > saldo:
      print(f"Saldo insuficiente! Disponivel: R$ {saldo:.2f}")
    
  if saldo == 0:
    print("Saldo esgotado. Sistema offline.")


main()
