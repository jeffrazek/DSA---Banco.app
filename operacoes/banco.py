from entidades.cliente import Cliente
from entidades.conta import Conta, ContaCorrente, ContaPoupanca

# Inicialização da clase
class Banco():

    # Construtor da classe Banco
    def __init__(self, nome_banco: str):
        self.nome_banco = nome_banco
        self._contas = {}
        self._clientes = {}

    # Cria cadastro inicial do cliente;
    def cadastro_cliente(self, nome: str, endereco: str, cpf: str) -> Cliente:

        # Verificando se já existe cadastro do cliente;
        if cpf in self._clientes:
            print("ERRO! Cliente com CPF já cadastrado.")
            return self._clientes[cpf]

        # Criando cadastro do cliente;
        novo_cliente = Cliente(nome, endereco, cpf)
        self._clientes[cpf] = novo_cliente

        print(f"\nCliente {nome} cadastrado com sucesso.\n")

        return novo_cliente

    # Cria conta baseado no cadastro do cliente já existente;
    def criar_conta(self, cliente: Cliente, tipo: str) -> Conta:

        # Criando numero da conta;
        numero_conta = Conta._total_contas + 1

        # Criando conta corrente;
        if tipo == "1":
            nova_conta = ContaCorrente(numero_conta, cliente)

        # Criando conta poupança
        elif tipo == "2":
            nova_conta = ContaPoupanca(numero_conta, cliente)

        else:
            print("Tipo de conta não existe.")
            return None

        # Adiciona a nova conta ao dicionário de contas
        self._contas[numero_conta] = nova_conta

        # Associa a conta ao cliente
        cliente.adicionar_conta(nova_conta)
        print(f"\nConta {nova_conta.tipo} numero {numero_conta} criada para {cliente.nome} com sucesso.\n")

        return nova_conta

    # Busca informações do cliente na base de dados;
    def get_cliente(self, cpf):
        if cpf in self._clientes:
            return self._clientes.get(cpf)