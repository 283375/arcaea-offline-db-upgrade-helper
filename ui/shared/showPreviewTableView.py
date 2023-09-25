from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QTableView


def showPreviewTableView(tbv: QTableView):
    screen = QGuiApplication.primaryScreen()
    screenGeometry = screen.availableGeometry()

    w = round(screenGeometry.width() * 0.75)
    h = round(screenGeometry.height() * 0.6)

    x = screenGeometry.width() / 2 - w / 2
    y = screenGeometry.height() / 2 - h / 2

    tbv.setWindowFlag(Qt.WindowType.Window, True)
    tbv.setSelectionMode(QTableView.SelectionMode.NoSelection)
    tbv.resizeRowsToContents()
    tbv.resizeColumnsToContents()
    tbv.show()
    tbv.setGeometry(x, y, w, h)
