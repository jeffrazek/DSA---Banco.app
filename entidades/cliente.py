class Cliente:
    def __init__(self, nome: str, endereco: str, cpf: str):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)