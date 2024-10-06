
class Nodo:
    """Esta classe representa um nodo de uma estrutura duplamente encadeada."""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class Fila:
    """Esta classe representa uma fila usando uma estrutura encadeada."""

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def push(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        if self.ultimo is None:  # Fila está vazia
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo

    def pop(self):
        if self.primeiro is None:
            raise IndexError("pop de uma fila vazia")
        remover_nodo = self.primeiro
        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None
        return remover_nodo.dado

    def busca(self, valor):
        atual = self.primeiro
        posicao = 0
        while atual is not None:
            if atual.dado == valor:
                return posicao
            atual = atual.proximo
            posicao += 1
        raise ValueError("O valor não está na fila")

    def percorre_imprime(self):
        atual = self.primeiro
        while atual is not None:
            print(atual.dado, end=" ")
            atual = atual.proximo
        print()

    def inverte(self):
        atual = self.primeiro
        anterior = None
        self.ultimo = self.primeiro  # Novo último nodo será o antigo primeiro
        while atual is not None:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo
        self.primeiro = anterior


fila = Fila()
fila.push(1)
fila.push(4)
fila.push(5)
fila.push(2)
fila.percorre_imprime()
fila.inverte()
fila.percorre_imprime()