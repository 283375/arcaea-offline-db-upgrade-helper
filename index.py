import sys

from PySide6.QtWidgets import QApplication

from ui.mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())
