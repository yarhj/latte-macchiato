import sys
from PyQt6.QtWidgets import QApplication

from table import Cappuccino


def main():
    app = QApplication(sys.argv)
    ex = Cappuccino()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
