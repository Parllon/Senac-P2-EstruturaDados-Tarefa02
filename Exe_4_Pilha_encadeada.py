

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

    def busca(self, valor):
        corrente = self.topo
        while corrente is not None:
            if corrente.dado == valor:
                return True
            corrente = corrente.anterior
        return False

    def remover_do_topo(self, placa_desejada):
        """Remove elementos do topo até encontrar a placa desejada."""
        corrente = self.topo
        elementos_removidos = []

        while corrente is not None:
            if corrente.dado == placa_desejada:
                break
            elementos_removidos.append(corrente.dado)
            self.remove()  # Remove o elemento do topo
            corrente = self.topo  # Atualiza a corrente para o novo topo

        if corrente is None:
            # Se não encontrou a placa, restaura os elementos removidos
            for dado in reversed(elementos_removidos):
                self.insere(dado)
            return None  # A condição não foi atendida

        return elementos_removidos


placa_carro = Pilha()

placa_carro.insere(1530)
placa_carro.insere(4530)
placa_carro.insere(6318)
placa_carro.insere(7709)
placa_carro.insere(5630)

# Verifica se um carro pode ser liberado
placa_desejada = 6318
carros_remover = placa_carro.remover_do_topo(placa_desejada)

if carros_remover is not None:
    print(f"O carro foi estacionado na rua {placa_desejada}, remova os seguintes carros: {carros_remover} para poder sair.")
else:
    print(f"O carro com a placa {placa_desejada} não foi encontrado.")