import sqlite3

from arcaea_offline.database import Database
from PySide6.QtCore import QDateTime, QUrl, Slot
from PySide6.QtWidgets import QMessageBox, QWidget
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

from ..dbPreview.v4 import Score, ScoresV4TableModel, ScoresV4TableView
from ..shared.showPreviewTableView import showPreviewTableView
from .V1ToV4_ui import Ui_DbConvert_V1ToV4


def getV1Conn(path: str):
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA journal_mode=memory;")
    return conn


def checkV1DatabaseEntries(path: str) -> int | None:
    conn = getV1Conn(path)
    result = False
    with conn:
        cursor = conn.cursor()
        # test table
        try:
            cursor.execute(
                "SELECT id, song_id, rating_class, score, pure, far, lost, time, max_recall, clear_type FROM scores"
            )
        except Exception:
            result = False
        result = cursor.execute("SELECT COUNT(id) FROM scores").fetchone()[0]
    conn.close()
    return result


def convertV1EntriesToV4(
    path: str, *, setDateNone: bool = True, comment: str | None = None
) -> list[Score]:
    thresholdTimestamp = QDateTime.fromString(
        "2017-01-23 00:00:00", "yyyy-MM-dd hh:mm:ss"
    ).toSecsSinceEpoch()

    conn = getV1Conn(path)
    with conn:
        cursor = conn.cursor()
        entries = cursor.execute(
            "SELECT song_id, rating_class, score, pure, far, lost, time, max_recall FROM scores"
        ).fetchall()
        new_scores = []
        for song_id, rating_class, score, pure, far, lost, time, max_recall in entries:
            if setDateNone:
                new_date = None if time <= thresholdTimestamp else time
            else:
                new_date = time

            new_max_recall = (
                max_recall if max_recall is not None and max_recall >= 0 else None
            )
            new_scores.append(
                Score(
                    song_id=song_id,
                    rating_class=rating_class,
                    score=score,
                    pure=pure,
                    far=far,
                    lost=lost,
                    date=new_date,
                    max_recall=new_max_recall,
                    comment=comment or None,
                )
            )
    conn.close()
    return new_scores


class DbConvert_V1ToV4(Ui_DbConvert_V1ToV4, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.v1DatabaseFileSelector.filesSelected.connect(self.checkV1Database)

    @property
    def v1DatabaseFile(self):
        if not self.v1DatabaseFileSelector.selectedFiles():
            return None
        return self.v1DatabaseFileSelector.selectedFiles()[0]

    @property
    def v4DatabaseFile(self):
        if not self.v4DatabaseFileSelector.selectedFiles():
            return None
        return self.v4DatabaseFileSelector.selectedFiles()[0]

    def checkV1Database(self):
        if not self.v1DatabaseFile:
            return

        scoreNum = checkV1DatabaseEntries(self.v1DatabaseFile)
        if scoreNum != False:
            QMessageBox.information(
                self, None, f"[V1 Database] Score table detected, {scoreNum} entries."
            )
        else:
            QMessageBox.critical(self, None, "[V1 Database] Cannot parse score table.")

    def getConvertedScores(self):
        return convertV1EntriesToV4(
            self.v1DatabaseFile,
            setDateNone=self.setDateNoneCheckBox.isChecked(),
            comment=self.commentTextEdit.toPlainText()
            if self.commentCheckBox.isChecked()
            else None,
        )

    @Slot()
    def on_previewButton_clicked(self):
        if not self.v1DatabaseFile:
            QMessageBox.critical(self, None, "Select a V1 database file first.")
            return

        model = ScoresV4TableModel(self)
        scores = self.getConvertedScores()
        [model.appendScore(score) for score in scores]

        tableView = ScoresV4TableView(self)
        tableView.setModel(model)
        showPreviewTableView(tableView)

    @Slot()
    def on_transferButton_clicked(self):
        if not self.v4DatabaseFile:
            QMessageBox.critical(self, None, "Select a V4 database file first.")
            return

        fileUrl = QUrl.fromLocalFile(self.v4DatabaseFile)
        sqliteUrl = fileUrl.toString().replace("file://", "sqlite://")
        confirm = QMessageBox.warning(
            self,
            "Before you continue...",
            f"Please make sure that you have selected the right databases.\n\n"
            f"V1: {self.v1DatabaseFile}\n"
            f"V4: {self.v4DatabaseFile}\n"
            f"V4(url): {fileUrl}\n\n"
            f"We have found {len(self.getConvertedScores())} score entries in V1 database.\n"
            "By continuing, you confirm that you have backed up both of your databases, "
            "and knowing the existing database may get corrupted after a failure transfer.",
            QMessageBox.StandardButton.Yes,
            QMessageBox.StandardButton.No,
        )

        if confirm != QMessageBox.StandardButton.Yes:
            QMessageBox.information(
                self, None, "You have cancelled the transfer operation."
            )
            return

        try:
            db = Database(create_engine(sqliteUrl, poolclass=NullPool))
            scores = self.getConvertedScores()
            with db.sessionmaker() as session:
                for score in scores:
                    session.add(score)
                session.commit()
            QMessageBox.information(self, None, "Transfer complete.")
        except Exception as e:
            QMessageBox.critical(self, None, "Transfer error:\n" + str(e))
