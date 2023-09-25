from typing import Any, Callable

from arcaea_offline.models import Score
from PySide6.QtCore import QDateTime, QLocale, Qt
from PySide6.QtGui import QColor, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QTableView


class ScoresV4TableModel(QStandardItemModel):
    HEADERS = [
        "song_id",
        "rating_class",
        "score",
        "pure",
        "far",
        "lost",
        "date",
        "max_recall",
        "clear_type",
        "modifier",
        "comment",
    ]
    RATING_CLASS_TEXT = ["PST", "PRS", "FTR", "BYD"]
    CLEAR_TYPE_TEXT = [
        "TRACK LOST",
        "NORMAL CLEAR",
        "FULL RECALL",
        "PURE MEMORY",
        "EASY CLEAR",
        "HARD CLEAR",
    ]
    MODIFIER_TEXT = ["NORMAL", "EASY", "HARD"]

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return self.HEADERS[section]

        return super().headerData(section, orientation, role)

    def columnCount(self, parent=None) -> int:
        return 11

    def convertScoreValueToStandardItem(
        self,
        value,
        *,
        displayRoleConverter: Callable[[Any], str] | None = None,
        textMappingList: list[str] | None = None,
    ):
        item = QStandardItem()

        if value is not None:
            item.setData(value)
            if textMappingList:
                displayRole = f"{value} ({textMappingList[value]})"
            elif displayRoleConverter:
                displayRole = f"{value} ({displayRoleConverter(value)})"
            else:
                displayRole = value
            item.setData(displayRole, Qt.ItemDataRole.DisplayRole)
        else:
            item.setData(None)
            item.setData("/", Qt.ItemDataRole.DisplayRole)
            item.setData(QColor("#9e9e9e"), Qt.ItemDataRole.ForegroundRole)
        return item

    def appendScore(self, score: Score):
        items = [
            self.convertScoreValueToStandardItem(score.song_id),
            self.convertScoreValueToStandardItem(
                score.rating_class, textMappingList=self.RATING_CLASS_TEXT
            ),
            self.convertScoreValueToStandardItem(score.score),
            self.convertScoreValueToStandardItem(score.pure),
            self.convertScoreValueToStandardItem(score.far),
            self.convertScoreValueToStandardItem(score.lost),
            self.convertScoreValueToStandardItem(
                score.date,
                displayRoleConverter=lambda n: QDateTime.fromSecsSinceEpoch(n).toString(
                    QLocale.system().dateTimeFormat(QLocale.FormatType.LongFormat)
                ),
            ),
            self.convertScoreValueToStandardItem(score.max_recall),
            self.convertScoreValueToStandardItem(
                score.clear_type, textMappingList=self.CLEAR_TYPE_TEXT
            ),
            self.convertScoreValueToStandardItem(
                score.modifier, textMappingList=self.MODIFIER_TEXT
            ),
            self.convertScoreValueToStandardItem(score.comment),
        ]

        self.appendRow(items)


class ScoresV4TableView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
