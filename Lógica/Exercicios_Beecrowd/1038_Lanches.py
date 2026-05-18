def main():
  codigo, quantidade = map(int, input().split())

  lanches = {
      1: 4.00,
      2: 4.50,
      3: 5.00,
      4: 2.00,
      5: 1.50
  }

  valor_total = lanches[codigo] * quantidade

  print(f"Total: R$ {valor_total:.2f}")

main()
