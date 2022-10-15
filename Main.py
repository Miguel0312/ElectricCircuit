import sys
from Circuit import Circuit
from PySide6.QtWidgets import QApplication
from Window import Window

def main():
    app = QApplication()
    mainCircuit = Circuit()
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()