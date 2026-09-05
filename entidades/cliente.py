class Cliente:
    def __init__(self, nome, endereco, cpf):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)