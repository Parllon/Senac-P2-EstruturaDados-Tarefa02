

class Nodo:
# Esta classe representa um nodo de uma estrutura encadeada.
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)

class Pilha:
    # Esta classe representa uma pilha usando uma estrutura encadeada.
    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def insere(self, novo_dado):
        '''Insere um elemento no final da pilha.'''
        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(novo_dado)
        # Faz com que o novo nodo seja o topo da pilha.
        novo_nodo.anterior = self.topo
        # Faz com que a cabeça da lista referencie o novo nodo.
        self.topo = novo_nodo

    def remove(self):
        assert self.topo

        self.topo = self.topo.anterior

    def maior_elemento(self):
        """Retorna o maior elemento da pilha."""
        if self.topo is None:
            raise ValueError("A pilha está vazia!")

        maior = float('-inf')  # Inicializa como o menor valor possível
        corrente = self.topo

        while corrente is not None:
            maior = max(maior, corrente.dado)  # Atualiza o maior valor se necessário
            corrente = corrente.anterior  # Move para o próximo nodo

        return maior


pilha = Pilha()
pilha.insere(3)
pilha.insere(1)
pilha.insere(4)
pilha.insere(1)
pilha.insere(15)
pilha.insere(9)
pilha.insere(2)
pilha.insere(6)

print("Pilha:", pilha)
print("Maior elemento da pilha:", pilha.maior_elemento())