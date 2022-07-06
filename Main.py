from Circuit import Circuit
from Node import Node
from Resistance import Resistance
from Generator import Generator

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

    c.addComponent(g)
    c.addComponent(r1)
    c.addComponent(r2)

    for n in c.getNodes():
        print(n.getID())
    
    print(g.getTension())
    print(r1.getResistance())
    print(r2.getResistance())

if __name__ == "__main__":
    main()