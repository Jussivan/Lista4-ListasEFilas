def filtrar_strings(lista):
    nova_lista = []
    for string in lista:
        if len(string) > 5:
            nova_lista.append(string)
    return nova_lista

strings = ["Python", "Programação", "OpenAI", "ChatGPT", "Linguagem"]
resultado = filtrar_strings(strings)
print(resultado)