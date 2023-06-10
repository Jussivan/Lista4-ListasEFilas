from Fila import Fila

fila = Fila()
print("Digite uma sequência de números inteiros (Digite um número negativo para parar):")
while True:
    numero = int(input())
    if numero < 0:
        break
    fila.inserir(numero)
print("\nNúmeros inseridos na fila:")
while not fila.esta_vazia():
    item = fila.remover()
    print(item)