def main():
    precos_antigos = [50.0, 150.0, 80.0, 200.0, 95.0]
    precos_reajustados = [preco + (preco * 10/100) if preco >= 100 else preco - (preco * 5/100) for preco in precos_antigos]

    print(f"Os preços são: {precos_antigos}")
    print(f"Os preços reajustados são: {precos_reajustados}")
main()
