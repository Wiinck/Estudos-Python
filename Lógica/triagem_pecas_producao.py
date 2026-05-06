def main():
  
  for lote in range(1, 16):
    if lote == 10: 
      print(f"Peca {lote}: UNIDADE DE TESTE - DESCARTAR")
      continue

    if lote % 2 == 0:
      print(f"Peca {lote}: Setor A")

    else:
      print(f"Peca {lote}: Setor B")

main()
