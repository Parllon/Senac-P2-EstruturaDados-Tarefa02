class Processo:
    def __init__(self, Id, name, priority, wait):
        self.Id = Id
        self.name = name
        self.priority = priority
        self.wait = wait

    def __repr__(self):
        return f"{{Id: {self.Id}, Name: '{self.name}', Priority: {self.priority}, Wait: {self.wait}}}"


class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def push(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        if self.ultimo is None:
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
        self.ultimo = self.primeiro
        while atual is not None:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo
        self.primeiro = anterior

    def matar_maior_espera(self):
        if self.primeiro is None:
            raise IndexError("Nenhum processo para matar na fila vazia")

        atual = self.primeiro
        maior_espera = atual
        anterior = None
        anterior_maior_espera = None

        while atual.proximo is not None:
            if atual.proximo.dado.wait > maior_espera.dado.wait:
                maior_espera = atual.proximo
                anterior_maior_espera = atual
            atual = atual.proximo

        if maior_espera == self.primeiro:
            self.primeiro = self.primeiro.proximo
            if self.primeiro is None:
                self.ultimo = None
        else:
            anterior_maior_espera.proximo = maior_espera.proximo
            if maior_espera == self.ultimo:
                self.ultimo = anterior_maior_espera


# Exemplo de uso
fila = Fila()
fila.push(Processo(104, "Windows Manager", 4, 20))
fila.push(Processo(105, "Chrome Browser", 2, 15))
fila.push(Processo(106, "Python Script", 1, 25))
fila.percorre_imprime()
fila.matar_maior_espera()
fila.percorre_imprime()
fila.pop()
fila.percorre_imprime()
