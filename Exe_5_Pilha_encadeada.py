class Pilha:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return self.itens == []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None

def TPilha2(pilha_N, pilha_P, vetor):
    for numero in vetor:
        if numero >= 1:
            pilha_P.empilhar(numero)
        elif numero <= -1:
            pilha_N.empilhar(numero)

# Exemplo de uso:
N = Pilha()
P = Pilha()
vetor = [1, -2, 0, 3, -4, 0, 5, -6, 30, -35, 70, 6, -1]

TPilha2(N, P, vetor)

print("Pilha N:", N.itens)
print("Pilha P:", P.itens)

