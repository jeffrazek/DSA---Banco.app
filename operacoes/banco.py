from entidades.cliente import Cliente
from entidades.conta import Conta, ContaCorrente, ContaPoupanca

class Banco():
    def __init__(self, nome: str):
        self.nome = nome
        self.contas = {}
        self.clientes = {}

    def cadastro_cliente(self, nome: str, cpf: str) -> Cliente:
        if cpf in self.clientes:
            print("ERRO! Cliente com CPF já cadastrado.")
            return self.clientes[cpf]