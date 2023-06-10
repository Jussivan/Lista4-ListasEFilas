import random

class No:
    def __init__(self, numero):
        self.numero = numero
        self.proximo = None

class Roleta:
    def __init__(self):
        self.head = None

    def adicionar_numero(self, numero):
        novo_no = No(numero)
        if self.head is None:
            self.head = novo_no
            novo_no.proximo = novo_no
        else:
            atual = self.head
            while atual.proximo != self.head:
                atual = atual.proximo
            atual.proximo = novo_no
            novo_no.proximo = self.head

    def girar_roleta(self):
        if self.head is None:
            print("A roleta está vazia.")
            return

        numero_sorteado = random.choice(self.obter_numeros())
        print("Número sorteado:", numero_sorteado)

        atual = self.head
        while True:
            if atual.numero == numero_sorteado:
                print("Parabéns! Você ganhou.")
                return
            atual = atual.proximo
            if atual == self.head:
                break

        print("Você perdeu. Tente novamente.")

    def obter_numeros(self):
        numeros = []
        if self.head is None:
            return numeros

        atual = self.head
        while True:
            numeros.append(atual.numero)
            atual = atual.proximo
            if atual == self.head:
                break

        return numeros

roleta = Roleta()
numeros_roleta = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22,
                  18, 29, 7, 28, 12, 35, 3, 26]
for numero in numeros_roleta:
    roleta.adicionar_numero(numero)
print("Bem-vindo à Roleta!")
print("Números disponíveis:", roleta.obter_numeros())
while True:
    aposta = int(input("Faça sua aposta (digite um número da roleta): "))
    roleta.girar_roleta()
    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() != "s":
        break