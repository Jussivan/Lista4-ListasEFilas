class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
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
            self.primeiro = novo_no

    def inserir_final(self, valor):
        novo_no = No(valor)
        if self.esta_vazia():
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            self.ultimo.proximo = novo_no
            self.ultimo = novo_no

    def remover_inicio(self):
        if self.esta_vazia():
            print("A lista está vazia. Não é possível remover elementos.")
        else:
            removido = self.primeiro
            self.primeiro = self.primeiro.proximo
            if self.primeiro is None:
                self.ultimo = None
            return removido.valor

    def remover_final(self):
        if self.esta_vazia():
            print("A lista está vazia. Não é possível remover elementos.")
        else:
            removido = self.ultimo
            if self.primeiro == self.ultimo:
                self.primeiro = None
                self.ultimo = None
            else:
                atual = self.primeiro
                while atual.proximo != self.ultimo:
                    atual = atual.proximo
                atual.proximo = None
                self.ultimo = atual
            return removido.valor

    def exibir_lista(self):
        if self.esta_vazia():
            print("A lista está vazia.")
        else:
            atual = self.primeiro
            while atual is not None:
                print(atual.valor, end=" -> ")
                atual = atual.proximo
            print("None")