from abc import ABC, abstractmethod

class Conta(ABC):

    _total_contas = 0

    def __init__(self, numero: int, cliente: str):
        self.numero = numero
        self.cliente = cliente
        self._saldo = 0.0
        self._historico = []
        Conta._total_contas +=1

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito não permitido!")
        else:
            valor += self._saldo
            print("Depósito efetuado com sucesso.")

    @abstractmethod
    def sacar(self, valor: int):
        pass

    def ver_saldo(self):
        return self._saldo

    def ver_historico(self):
        return self._historico


class ContaPoupanca(Conta):
    def __init__(self, numero: int, cliente):
        super().__init__(numero, cliente)
        self.tipo = "Poupança"

    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficente.")
        else:
            self._saldo -= valor
            print("Saque efetuado com sucesso.")

class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: str, chequeEspecial = 500):
        self.limite = chequeEspecial
        super().__init__(numero, cliente)
        self.tipo = "Corrente"

    def sacar(self, valor: int):
        if valor <= self._saldo + self.limite:
            self._saldo -= valor
        else:
            print("Valor de saque não permitido!")