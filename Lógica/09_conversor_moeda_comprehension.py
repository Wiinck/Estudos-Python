def main():
  precos_dolar = [10.0, 50.0, 100.0, 5.0]
  precos_real = [preco_dol * 5.20 for preco_dol in precos_dolar]

  print(f"Preços em dólar: {precos_dolar}")
  print(f"Precos em real: {precos_real}")

main()
