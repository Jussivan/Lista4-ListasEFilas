from Fila import Fila
fila = Fila()
while True:
    print("======= MENU =======")
    print("1. Adicionar número na fila")
    print("2. Remover número da fila")
    print("3. Tamanho da fila")
    print("4. Mostrar fila")
    print("0. Sair")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        numero = int(input("Digite o número a ser adicionado na fila: "))
        fila.adicionar(numero)
        print("Número adicionado na fila.")
    elif opcao == "2":
        numero_removido = fila.remover()
        if numero_removido is not None:
            print("Número removido da fila:", numero_removido)
        else:
            print("A fila está vazia.")
    elif opcao == "3":
        tamanho = fila.tamanho()
        print("Tamanho da fila:", tamanho)
    elif opcao == "4":
        fila.mostrar_fila()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Digite novamente.")
    print()
print("Programa encerrado.")