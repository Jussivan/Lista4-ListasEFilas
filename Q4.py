from Fila import Fila

def verificar_palindromo(frase):
    fila = Fila()
    for caractere in frase:
        fila.inserir(caractere)
    frase_reversa = ""
    while not fila.esta_vazia():
        frase_reversa += fila.remover()
    return frase == frase_reversa

frase = input("Digite uma frase: ")
frase = frase.lower().replace(" ", "")
if verificar_palindromo(frase):
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")