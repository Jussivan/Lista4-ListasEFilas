def elementos_comuns(lista1, lista2):
    elementos = []
    for elemento in lista1:
        if elemento in lista2:
            elementos.append(elemento)
    return elementos

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
resultado = elementos_comuns(lista1, lista2)
print(resultado)