from operacoes.banco import Banco

banco = Banco("Banco ABCD")

def menu_principal():
    print(f"\nBem vindo ao {banco.nome_banco}.\n")
    print("1 - Criar cadastro de cliente:")
    print("2 - Criar conta:")
    print("3 - Consultar dados:")
    print("4 - SAIR\n")

    return input("Digite a opção desejada: ")

def consulta(dado):
    dado = input('Digite o CPF para verificar o cadastro: ')
    cliente = banco.get_cliente(dado)
    if cliente:
        print('\nCliente localizado:\n')
        print(f"Nome: {cliente.nome}")
        print(f"Endereço: {cliente.endereco}")
        print(f"CPF: {cliente.cpf}")
        for conta in cliente.contas:
            print(f"Tipo: {conta.__class__.__name__}, Número: {conta.numero}\n")


def main():

    
    while True:
        opcao = menu_principal()

        if opcao == '1':
            nome = input("Digite seu nome: ")
            endereco = input("Digite seu endereço: ")
            cpf = input("Digite seu CPF: ")
            banco.cadastro_cliente(nome, endereco, cpf)

        elif opcao == '2':
            cpf = input("Digite seu CPF: ")
            cliente = banco._clientes.get(cpf)

            if cliente:
                tipo_conta = input("Digite o tipo de conta desejada (corrente = 1/poupança = 2): ")
                banco.criar_conta(cliente, tipo_conta)

            else:
                print("Cliente inexistente!")

        elif opcao == '3':
            consulta(cpf)

        elif opcao == '4':
            print("\nATÉ MAIS!\n")
            break

        else:
            print("Opção incorreta. Digite uma das opções acima.")


if __name__ == "__main__":
    main()