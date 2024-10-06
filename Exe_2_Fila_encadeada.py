
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

fila = Fila()
fila.push(10)
fila.push(20)
fila.push(30)
print(fila.busca(20))
print(fila.busca(10))
print(fila.busca(30))