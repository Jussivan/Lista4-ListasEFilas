class Cliente:
    def __init__(self, nome, conta, saldo):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo
        self.proximo = None

class ListaEncadeadaClientes:
    def __init__(self):
        self.primeiro = None

    def esta_vazia(self):
        return self.primeiro is None

    def inserir_cliente(self, nome, conta, saldo):
        novo_cliente = Cliente(nome, conta, saldo)
        novo_cliente.proximo = self.primeiro
        self.primeiro = novo_cliente

    def remover_cliente(self, conta):
        if self.esta_vazia():
            print("A lista está vazia. Não é possível remover clientes.")
            return

        if self.primeiro.conta == conta:
            removido = self.primeiro
            self.primeiro = self.primeiro.proximo
            removido.proximo = None
            print("Cliente removido:", removido.nome)
            return

        atual = self.primeiro
        while atual.proximo is not None:
            if atual.proximo.conta == conta:
                removido = atual.proximo
                atual.proximo = removido.proximo
                removido.proximo = None
                print("Cliente removido:", removido.nome)
                return
            atual = atual.proximo

        print("Cliente não encontrado.")

    def pesquisar_cliente(self, conta):
        if self.esta_vazia():
            print("A lista está vazia. Não é possível pesquisar clientes.")
            return

        atual = self.primeiro
        while atual is not None:
            if atual.conta == conta:
                print("Cliente encontrado:")
                print("Nome:", atual.nome)
                print("Número da conta:", atual.conta)
                print("Saldo:", atual.saldo)
                return
            atual = atual.proximo

        print("Cliente não encontrado.")

    def exibir_lista(self):
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        print("Lista de clientes:")
        print("{:<15} {:<15} {:<15}".format("Nome", "Conta", "Saldo"))
        print("---------------------------------------")
        atual = self.primeiro
        while atual is not None:
            print("{:<15} {:<15} R$ {:.2f}".format(atual.nome, atual.conta, atual.saldo))
            atual = atual.proximo
        print()

lista_clientes = ListaEncadeadaClientes()
lista_clientes.inserir_cliente("João", 123456, 1000.0)
lista_clientes.inserir_cliente("Maria", 987654, 500.0)
lista_clientes.inserir_cliente("Pedro", 567890, 1500.0)
lista_clientes.exibir_lista()
lista_clientes.remover_cliente(987654)
lista_clientes.exibir_lista()