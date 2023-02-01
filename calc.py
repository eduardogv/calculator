import sys

from PyQt6.QtWidgets import QApplication

from view import View

def main():
    calc = QApplication(sys.argv)

    view = View()
    view.show()
    #Model()
    #Controller()

    sys.exit(calc.exec())

if __name__ == '__main__':
    main()