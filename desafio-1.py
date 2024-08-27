class Conta:
    def __init__(self):
        self.saldo = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f}")
            print(f"Depositado R${valor:.2f}. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                self.extrato.append(f"Saque: R${valor:.2f}")
                print(f"Sacado R${valor:.2f}. Saldo atual: R${self.saldo:.2f}")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor de saque deve ser positivo.")

    def extrato(self):
        print("Extrato:")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo final: R${self.saldo:.2f}")

def main():
    conta = Conta()
    while True:
        print("\nEscolha uma opção:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")

        opcao = input("Digite o número da opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor do depósito: "))
            conta.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor do saque: "))
            conta.sacar(valor)
        elif opcao == '3':
            conta.extrato()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
