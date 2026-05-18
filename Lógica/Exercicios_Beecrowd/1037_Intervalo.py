def main():
    num = float(input())
    intervalos = ([0,25], [25,50], [50,75], [75,100])

    if num >= 0 and num <= 25.00000:
        print(f"Intervalo [0,25]")
    elif num > 25.00000 and num <= 50.0000000:
        print(f"Intervalo (25,50]")
    elif num > 50.0000000 and num <= 75.0000000:
        print(f"Intervalo (50,75]")
    elif num > 75.0000000 and num <= 100.0000000:
        print(f"Intervalo (75,100]")
    else:
      print("Fora de intervalo")




main()
