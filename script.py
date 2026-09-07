from operacoes.banco import Banco

def menu_principal():
    print("\nBem vindo.\n")
    print("1 - Criar cadastro de cliente:")
    print("2 - Criar conta:")
    print("3 - ")
    print("4 - SAIR\n")

    return input("Digite uma opção: ")

def main():

    banco = Banco("Banco ABCD")

    while True:
        opcao = menu_principal()

        if opcao == '1':
            nome = input("Digite o nome: ")
            endereco = input("Digite o endereço: ")
            cpf = input("Digite o CPF: ")
            banco.cadastro_cliente(nome, endereco, cpf)

        elif opcao == '2':
            cpf = input("Digite seu CPF: ")
            cliente = banco._clientes.get(cpf)

            if cliente:
                tipo = input("Digite o tipo de conta desejada (corrente/poupança): ")
                banco.criar_conta(cliente, tipo)

            else:
                print("Cliente inexistente!")

        elif opcao == '3':
            break

        elif opcao == '4':
            print("ATÉ MAIS!")
            break

        else:
            print("Opção incorreta. Digite uma das opções acima.")


if __name__ == "__main__":
    main()