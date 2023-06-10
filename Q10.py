class No:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None

class ListaEncadeadaDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def esta_vazia(self):
        return self.primeiro is None

    def inserir_inicio(self, valor):
        novo_no = No(valor)
        if self.esta_vazia():
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            novo_no.proximo = self.primeiro
            self.primeiro.anterior = novo_no
            self.primeiro = novo_no

    def inserir_final(self, valor):
        novo_no = No(valor)
        if self.esta_vazia():
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            novo_no.anterior = self.ultimo
            self.ultimo.proximo = novo_no
            self.ultimo = novo_no

    def remover_inicio(self):
        if self.esta_vazia():
            print("A lista está vazia. Não é possível remover elementos.")
            return

        removido = self.primeiro
        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None
        else:
            self.primeiro.anterior = None

        return removido.valor

    def remover_final(self):
        if self.esta_vazia():
            print("A lista está vazia. Não é possível remover elementos.")
            return

        removido = self.ultimo
        self.ultimo = self.ultimo.anterior
        if self.ultimo is None:
            self.primeiro = None
        else:
            self.ultimo.proximo = None

        return removido.valor

    def exibir_lista(self):
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        atual = self.primeiro
        while atual is not None:
            print(atual.valor, end=" <-> ")
            atual = atual.proximo
        print("None")