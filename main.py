from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QObject
from mainwindow_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
import sys


class MainWindow(QMainWindow, QObject):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
