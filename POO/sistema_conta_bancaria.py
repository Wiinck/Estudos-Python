class Titular:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def exibir_saldo(self):
        return f"Olá {self.nome} seu saldo é R${self.saldo:.2f}."

    def depositar(self, valor):
        self.valor = valor
        if valor > 0:
            self.saldo += self.valor
            return f"O saldo após o depósito de R${self.valor:.2f} é de R${self.saldo:.2f}"

    def sacar(self, valor):
        self.valor = valor
        if valor > 0:
            self.saldo -= self.valor
            return f"O saldo após o saque de R${self.valor:.2f} é de R${self.saldo:.2f}"
            
        else:
            return "Saldo insuficiente!"
        

def main():
    minha_conta = Titular("Matheus", 480000)

    print(minha_conta.exibir_saldo())
    
    print(minha_conta.depositar(500))
    print(minha_conta.exibir_saldo())
    
    print(minha_conta.sacar(2000))

main()
