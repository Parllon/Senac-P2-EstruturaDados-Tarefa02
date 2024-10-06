class NodoLista:

    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class ListaEncadeada:
    """Esta classe representa uma lista encadeada"""

    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def insere_no_inicio(lista, novo_dado):
        # 1 - Cria um novo nodo com o dado a ser armazenado
        novo_nodo = NodoLista(novo_dado)
        # 2 - Faz com que o novo nodo seja a cabeça da lista
        novo_nodo.proximo = lista.cabeca
        # 3 - Faz com que a cabeça da lista referencie o novo nodo
        lista.cabeca = novo_nodo

    def insere_depois(lista, nodo_anterior, novo_dado):
        assert nodo_anterior  # Nodo anterior precisa existir na lista

        # Cria um novo nodo com o dado desejado
        novo_nodo = NodoLista(novo_dado)
        # Faz o próximo do novo nodo ser o próximo do nodo anterior
        novo_nodo.proximo = nodo_anterior.proximo
        # Faz com que o novo nodo seja o próximo do nodo anterior
        nodo_anterior.proximo = novo_nodo

    def busca(lista, valor):
        corrente = lista.cabeca
        while corrente and corrente.dado != valor:
            corrente = corrente.proximo
        return corrente

    def remove(self, valor):
        nodo_a_remover = self.busca(valor)
        # Nodo a ser removido é a cabeça da lista.

        if self.cabeca == nodo_a_remover:
            self.cabeca = self.cabeca.proximo
        else:
            # Encontra a posição do elemento a ser removido.
            anterior = self.cabeca
            while anterior.proximo and anterior.proximo != nodo_a_remover:
                anterior = anterior.proximo
                # O nodo corrente é o nodo a ser removido.
            if anterior.proximo == nodo_a_remover:
                anterior.proximo = nodo_a_remover.proximo


lista = ListaEncadeada()
for i in range(11):
    lista.insere_no_inicio(i)
print("Lista:", lista)

lista.remove(5)
print("Lista:", lista)
