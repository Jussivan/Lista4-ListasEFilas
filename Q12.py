class Pessoa:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.anterior = None
        self.proximo = None

class AgendaTelefonica:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def esta_vazia(self):
        return self.primeiro is None

    def inserir_pessoa(self, nome, telefone):
        nova_pessoa = Pessoa(nome, telefone)
        if self.esta_vazia():
            self.primeiro = nova_pessoa
            self.ultimo = nova_pessoa
        else:
            nova_pessoa.anterior = self.ultimo
            self.ultimo.proximo = nova_pessoa
            self.ultimo = nova_pessoa

    def remover_pessoa(self, nome):
        if self.esta_vazia():
            print("A agenda está vazia. Não é possível remover pessoas.")
            return

        atual = self.primeiro
        while atual is not None:
            if atual.nome == nome:
                if atual == self.primeiro:
                    self.primeiro = atual.proximo
                    if self.primeiro is not None:
                        self.primeiro.anterior = None
                    else:
                        self.ultimo = None
                elif atual == self.ultimo:
                    self.ultimo = atual.anterior
                    if self.ultimo is not None:
                        self.ultimo.proximo = None
                    else:
                        self.primeiro = None
                else:
                    atual.anterior.proximo = atual.proximo
                    atual.proximo.anterior = atual.anterior
                return
            atual = atual.proximo

        print("Pessoa não encontrada na agenda.")

    def buscar_pessoa(self, nome):
        if self.esta_vazia():
            print("A agenda está vazia. Não é possível buscar pessoas.")
            return

        atual = self.primeiro
        while atual is not None:
            if atual.nome == nome:
                print("Pessoa encontrada na agenda:")
                print("Nome:", atual.nome)
                print("Telefone:", atual.telefone)
                return
            atual = atual.proximo

        print("Pessoa não encontrada na agenda.")

    def exibir_agenda(self):
        if self.esta_vazia():
            print("A agenda está vazia.")
            return

        atual = self.primeiro
        while atual is not None:
            print("Nome:", atual.nome)
            print("Telefone:", atual.telefone)
            print("---------------------------------------")
            atual = atual.proximo

agenda = AgendaTelefonica()
agenda.inserir_pessoa("João", "123456789")
agenda.inserir_pessoa("Maria", "987654321")
agenda.inserir_pessoa("Pedro", "567890123")
agenda.exibir_agenda()
agenda.remover_pessoa("Maria")
agenda.exibir_agenda()
