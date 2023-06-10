class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeadaCircular:
    def __init__(self):
        self.head = None

    def esta_vazia(self):
        return self.head is None

    def inserir_ordenado(self, dado):
        novo_no = No(dado)
        if self.esta_vazia():
            self.head = novo_no
            novo_no.proximo = novo_no
        elif dado <= self.head.dado:
            novo_no.proximo = self.head
            atual = self.head
            while atual.proximo != self.head:
                atual = atual.proximo
            atual.proximo = novo_no
            self.head = novo_no
        else:
            atual = self.head
            while atual.proximo != self.head and atual.proximo.dado < dado:
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no

    def primeiro_elemento(self):
        if self.esta_vazia():
            return None
        return self.head.dado

    def ultimo_elemento(self):
        if self.esta_vazia():
            return None
        atual = self.head
        while atual.proximo != self.head:
            atual = atual.proximo
        return atual.dado

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

lista = ListaEncadeadaCircular()
numeros = [10, 5, 8, 2, 15, 3]
for numero in numeros:
    lista.inserir_ordenado(numero)
lista.exibir_lista()
print("Primeiro elemento:", lista.primeiro_elemento())
print("Último elemento:", lista.ultimo_elemento())