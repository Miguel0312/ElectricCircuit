# ElectricCircuit

## Objective
This project allows the creation of an electric circuit through a GUI by inserting resistances, generator and wires. Then, with the press of a button all
the currents passing through each component and the tension of each node are calculated. This is done by writing the Kirchoff's Laws for each node and for
each loop in matrix form that are then solved using numpy.

## Usage
You can run the program by executing:
```
python3 Main.py
```
Drag and drop components from the top menu to build your circuit. Click on a component to open a menu on the bottom part of the window where the values
of the resistance and tension of the generators can be adjusted. The button on the right upper corner will trigger the calculations of currents and
tensions. Then, when clicking a component the bottom menu will show the tensions of the two nodes of the component and the intensity and direction of 
the current that is passing through it.
