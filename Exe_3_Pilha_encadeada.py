

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

    def pilha_inversa(self):
        """Imprime os elementos da pilha na ordem inversa."""
        pilha_temp = Pilha()
        nodo_atual = self.topo
        while nodo_atual is not None:
            pilha_temp.insere(nodo_atual.dado)
            nodo_atual = nodo_atual.anterior
        print("Elementos da pilha na ordem inversa:", end=" ")
        print(pilha_temp)

    def sao_iguais(self, outra_pilha):
        """Verifica se duas pilhas são iguais."""
        corrente1 = self.topo
        corrente2 = outra_pilha.topo

        while corrente1 is not None and corrente2 is not None:
            if corrente1.dado != corrente2.dado:
                return False
            corrente1 = corrente1.anterior
            corrente2 = corrente2.anterior

        # Verifica se ambas as pilhas foram completamente percorridas
        return corrente1 is None and corrente2 is None


pilha1 = Pilha()
for i in range(5):
    pilha1.insere(i)

pilha2 = Pilha()
for i in range(5):
    pilha2.insere(i)

print("Pilha 1:", pilha1)
print("Pilha 2:", pilha2)

print(pilha1.sao_iguais(pilha2))