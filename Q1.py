class Fila:
    def __init__(self):
        self.items = []

    def inserir(self, item):
        self.items.append(item)

    def remover(self):
        if not self.esta_vazia():
            return self.items.pop(0)
        else:
            return None

    def frente(self):
        if not self.esta_vazia():
            return self.items[0]
        else:
            return None

    def esta_vazia(self):
        return len(self.items) == 0