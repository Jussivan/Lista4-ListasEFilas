from ListaEncadeadaDupla import ListaEncadeadaDupla

lista_nomes = ListaEncadeadaDupla()
n = int(input("Digite a quantidade de nomes: "))
for i in range(n):
    nome = input("Digite o nome: ")
    lista_nomes.inserir_ordenado(nome)
lista_nomes.exibir_lista()