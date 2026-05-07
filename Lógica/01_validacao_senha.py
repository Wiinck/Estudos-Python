def main():
  tentativas = 3
  senha_acesso = 5637

  while tentativas > 0:
    senha = int(input("Digite a senha: "))

    if senha != senha_acesso:
      tentativas -= 1
      print("Senha inválida")
      print(f"Você tem mais {tentativas} tentativas!")

    if senha == senha_acesso:
      print("Seja Bem Vindo")
      break
    
  else:
    print("Acesso Bloqueado!")

main()
