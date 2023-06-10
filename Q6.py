import time

class Supermercado:
    def __init__(self):
        self.fila = []
        self.num_cliente = 0

    def adicionar_cliente(self):
        self.num_cliente += 1
        self.fila.append(self.num_cliente)

    def atender_cliente(self):
        if len(self.fila) > 0:
            cliente = self.fila.pop(0)
            print("Atendendo cliente:", cliente)
        else:
            print("Não há clientes na fila.")
            
supermercado = Supermercado()
while True:
    opcao = input("Pressione 'Enter' para adicionar um cliente ou digite 'sair' para encerrar o programa: ")
    if opcao.lower() == "sair":
        break
    supermercado.adicionar_cliente()
    time.sleep(5)
    supermercado.atender_cliente()