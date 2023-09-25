from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow

from .mainwindow_ui import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
