from ListaEncadeada import ListaEncadeada

def criar_lista_inversa(numeros):
    lista = ListaEncadeada()
    for numero in reversed(numeros):
        lista.inserir_inicio(numero)
    return lista

numeros = []
n = int(input("Digite a quantidade de números: "))
for i in range(n):
    numero = int(input("Digite o número: "))
    numeros.append(numero)
lista_inversa = criar_lista_inversa(numeros)
lista_inversa.exibir_lista()