def encontrar_palavra_mais_longa(lista):
    palavra_mais_longa = ""
    for palavra in lista:
        if len(palavra) > len(palavra_mais_longa):
            palavra_mais_longa = palavra
    return palavra_mais_longa

palavras = ["gato", "cachorro", "elefante", "leão", "tartaruga"]
resultado = encontrar_palavra_mais_longa(palavras)
print(resultado)