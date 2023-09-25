from PySide6.QtCore import QDir, QFileInfo, Qt, Signal, Slot
from PySide6.QtGui import QDragEnterEvent, QDragLeaveEvent, QDropEvent
from PySide6.QtWidgets import QFileDialog, QWidget

from .fileSelector_ui import Ui_FileSelector


class FileSelector(Ui_FileSelector, QWidget):
    accepted = Signal()
    filesSelected = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.reset()

        self.elidedLabel.setElideMode(Qt.TextElideMode.ElideMiddle)

        self.accepted.connect(self.filesSelected)
        self.accepted.connect(self.updateLabel)
        self.filesSelected.connect(self.updateLabel)

        self.__mode = self.getOpenFileNames

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls() and event.mimeData().urls()[0].isLocalFile():
            event.accept()
            self.elidedLabel.setText(
                f'Drop "{QFileInfo(event.mimeData().urls()[0].toLocalFile()).fileName()}"?'
            )
            return
        return super().dragEnterEvent(event)

    def dragLeaveEvent(self, event: QDragLeaveEvent):
        self.updateLabel()
        return super().dragLeaveEvent(event)

    def dropEvent(self, event: QDropEvent):
        url = event.mimeData().urls()[0]
        file = url.toLocalFile()
        self.selectFile(file)

    def getOpenFileNames(self):
        selectedFiles, filter = QFileDialog.getOpenFileNames(
            self,
            self.__caption,
            self.__startDirectory,
            self.__filter,
            "",
            options=self.__options,
        )
        if selectedFiles:
            self.__selectedFiles = selectedFiles
            self.accepted.emit()

    def getExistingDirectory(self):
        if selectedDir := QFileDialog.getExistingDirectory(
            self,
            self.__caption,
            self.__startDirectory,
            QFileDialog.Option.ShowDirsOnly | self.__options,
        ):
            self.__selectedFiles = [selectedDir]
            self.accepted.emit()

    def selectFile(self, filename: str):
        fileInfo = QFileInfo(filename)
        if not fileInfo.exists():
            return

        self.__selectedFiles = [fileInfo.absoluteFilePath()]
        self.__startDirectory = fileInfo.dir().absolutePath()
        self.filesSelected.emit()

    def selectedFiles(self):
        return self.__selectedFiles

    def setNameFilters(self, filters: list[str]):
        self.__filter = ";;".join(filters) if filters else ""

    def setOptions(self, options: QFileDialog.Option):
        self.__options = options

    def setMode(self, mode):
        if mode in [self.getOpenFileNames, self.getExistingDirectory]:
            self.__mode = mode
        else:
            raise ValueError("Invalid mode")

    def reset(self):
        self.__selectedFiles = []
        self.__caption = None
        self.__startDirectory = QDir.currentPath()
        self.__filter = ""
        self.__options = QFileDialog.Option(0)

        self.updateLabel()

    def updateLabel(self):
        if selectedFiles := self.selectedFiles():
            self.elidedLabel.setText("<br>".join(selectedFiles))
        else:
            self.elidedLabel.setText("...")

    @Slot()
    def on_selectButton_clicked(self):
        self.__mode()
