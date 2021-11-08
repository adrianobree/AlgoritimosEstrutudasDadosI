class Noverif():
    def __init__(self, data):
        self.data = data
        self.prox = None


class ListaLigada():
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, newNo):
        if self.head:
            pont = self.head
            while (pont.prox):
                pont = pont.prox
            pont.prox = newNo

        else:
            self.head = newNo

        self.size += 1

    def size(self):
        return self.size

    def search(self, elem):
        cont = 0
        pont = self.head
        for i in range(self.size):
            if (pont.data == elem):
                cont += 1
            pont = pont.prox
        return cont


def cycleTest(lv, n):
    comp = lv.head
    for i in range(n):
        resp = lv.search(comp.data)
        if (resp > 1):
            return 1
        comp = comp.prox
    return 0


lv = ListaLigada()
n = int(input())
for i in range(n):
    elem = int(input())
    test = Noverif(elem)

    lv.insert(test)

a = cycleTest(lv, n)
print(a)


