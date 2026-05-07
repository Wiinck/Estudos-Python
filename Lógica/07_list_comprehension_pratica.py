def main():
  precos = [100, 250, 400, 50]
  precos_com_desconto = [preco - 10 for preco in precos]

  print(f"Preco Original: {precos}")
  print(f"Preco com desconto: {precos_com_desconto}")

main()
