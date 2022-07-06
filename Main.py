from Circuit import Circuit
from Node import Node
from Resistance import Resistance
from Generator import Generator
from Wire import Wire

def main():
    c = Circuit()

    n1 = Node()
    n2 = Node()
    n3 = Node()

    c.addNode(n1)
    c.addNode(n2)
    c.addNode(n3)

    g = Generator(n1, n2, 12.0)
    r1 = Resistance(n2, n3, 1000.0)
    r2 = Resistance(n3, n1, 1000.0)
    r3 = Resistance(n3, n1, 1000.0)

    c.addComponent(g)
    c.addComponent(r1)
    c.addComponent(r2)
    c.addComponent(r3)

    cycles = c.getCycles()
    for cycle in cycles:
        print(" ".join([str(node) for node in cycle.nodes]))
    #print([c for c in cycles[1].components])

if __name__ == "__main__":
    main()