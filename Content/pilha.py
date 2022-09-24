class Pilha:

    def __init__(self):
        self.lista = []

    def isFull(self):
        return False

    def isEmpty(self):
        if len(self.lista) == 0:
            return True
        return False

    def put(self, info):
        self.lista.append(info)

    def pop(self):
        return self.lista.pop()

    def peek(self):
        pos = len(self.lista) - 1
        return self.lista[pos]            

