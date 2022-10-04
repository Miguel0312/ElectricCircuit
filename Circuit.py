import numpy as np
from Component import Component
from ComponentType import ComponentType
from Node import Node
from Path import Path

class Circuit:
    def __init__(self):
        self._nodes = []
        self._components = []

    def addNode(self, n: Node) -> None:
        self._nodes.append(n)
    
    def addComponent(self, c: Component) -> None:
        self._components.append(c)

    def getNodes(self) -> list[Node]:
        return self._nodes

    def getComponents(self) -> list[Component]:
        return self._components

    def getCycles(self) -> list[Node]:
        cycles = []
        for edge in self._components:
            for node in edge.getNodes():
                p = Path()
                p.nodes.append(node)
                self.findNewCycles(p, cycles)
        return cycles

    def findNewCycles(self, path: Path, cycles: list[Path]) -> None:
        start_node = path.nodes[0]
        next_node= None
        sub = []

        #visit each edge and each node of each edge
        for component in self._components:
            node1, node2 = component.getNodes()
            if start_node in [node1, node2]:
                    if node1 == start_node:
                        next_node = node2
                    else:
                        next_node = node1
                    if not path.visited(next_node):
                            # neighbor node not on path yet
                            sub = Path()
                            sub.addSegment(next_node, component)
                            sub.extend(path)
                            # explore extended path
                            self.findNewCycles(sub, cycles);
                    elif len(path.nodes)>1 and next_node == path.nodes[-1]:
                            sub = Path()
                            sub.addSegment(next_node, component)
                            sub.extend(path)
                            repeat = False
                            for c in sub.components:
                                if sub.components.count(c) != 1:
                                    repeat = True
                            if sub.isNew(cycles) and not repeat:
                                cycles.append(sub)

    def makeEquations(self, currentEquations: list[list[float]], voltageEquationsCoefficients: list[list[float]], voltageEquationsTerms: list[float]):
        coefficients = []
        for c in currentEquations:
            coefficients.append(c)
        for c in voltageEquationsCoefficients:
            coefficients.append(c)
        
        terms = []
        for _ in range(len(currentEquations)):
            terms.append([0])
        for t in voltageEquationsTerms:
            terms.append([t])
        
        return np.array(coefficients), np.array(terms)

    def solveCircuit(self):
        #Get equations from Kirchhoff's current law
        currentEquations = [[0]*len(self._components) for i in range(len(self._nodes))]
        for i in range(len(self._components)):
            n1, n2 = self._components[i].getNodes()
            currentEquations[self._nodes.index(n1)][i] = -1
            currentEquations[self._nodes.index(n2)][i] = 1

        #Get equations from Kirchhoff's voltage law
        cycles = self.getCycles()
        voltageEquationsCoefficients = [[0]*len(self._components) for _ in range(len(cycles))]
        voltageEquationsTerms = [0 for _ in range(len(cycles))]
        for j in range(len(cycles)):
            cycle = cycles[j]
            for i in range(len(cycle.components)):
                component = cycle.components[i]
                if component.getType() == ComponentType.resistance:
                    if component.getNodes()[0] == cycle.nodes[i]:
                        voltageEquationsCoefficients[j][self._components.index(cycle.components[i])] = component.getResistance()
                    else:
                        voltageEquationsCoefficients[j][self._components.index(cycle.components[i])] = -component.getResistance()
                if component.getType() == ComponentType.generator:
                    if component.getNodes()[0] == cycle.nodes[i]:
                        voltageEquationsTerms[j] -= component.getTension()
                    else:
                        voltageEquationsTerms[j] += component.getTension()
        
        #Solve the system using numpy utilities
        coefficients, terms = self.makeEquations(currentEquations, voltageEquationsCoefficients, voltageEquationsTerms)
        inverse = np.linalg.pinv(coefficients)
        print(np.matmul(inverse, terms))
