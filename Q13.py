class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeadaCircular:
    def __init__(self):
        self.head = None

    def esta_vazia(self):
        return self.head is None

    def inserir_inicio(self, dado):
        novo_no = No(dado)
        if self.esta_vazia():
            self.head = novo_no
            novo_no.proximo = novo_no
        else:
            atual = self.head
            while atual.proximo != self.head:
                atual = atual.proximo
            atual.proximo = novo_no
            novo_no.proximo = self.head
            self.head = novo_no

    def inserir_final(self, dado):
        novo_no = No(dado)
        if self.esta_vazia():
            self.head = novo_no
            novo_no.proximo = novo_no
        else:
            atual = self.head
            while atual.proximo != self.head:
                atual = atual.proximo
            atual.proximo = novo_no
            novo_no.proximo = self.head

    def remover_inicio(self):
        if self.esta_vazia():
            print("A lista está vazia. Não é possível remover elementos.")
            return

        if self.head.proximo == self.head:
            self.head = None
        else:
            atual = self.head
            while atual.proximo != self.head:
                atual = atual.proximo
            atual.proximo = self.head.proximo
            self.head = self.head.proximo

    def remover_final(self):
        if self.esta_vazia():
            print("A lista está vazia. Não é possível remover elementos.")
            return

        if self.head.proximo == self.head:
            self.head = None
        else:
            anterior = None
            atual = self.head
            while atual.proximo != self.head:
                anterior = atual
                atual = atual.proximo
            anterior.proximo = self.head
            atual = None

    def exibir_lista(self):
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        atual = self.head
        while True:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
            if atual == self.head:
                break
        print()