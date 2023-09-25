# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'V1ToV4.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from ui.shared.fileSelector import FileSelector

class Ui_DbConvert_V1ToV4(object):
    def setupUi(self, DbConvert_V1ToV4):
        if not DbConvert_V1ToV4.objectName():
            DbConvert_V1ToV4.setObjectName(u"DbConvert_V1ToV4")
        DbConvert_V1ToV4.resize(400, 300)
        DbConvert_V1ToV4.setWindowTitle(u"DbConvert_V1ToV4")
        self.verticalLayout_2 = QVBoxLayout(DbConvert_V1ToV4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(DbConvert_V1ToV4)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.v1DatabaseFileSelector = FileSelector(DbConvert_V1ToV4)
        self.v1DatabaseFileSelector.setObjectName(u"v1DatabaseFileSelector")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.v1DatabaseFileSelector.sizePolicy().hasHeightForWidth())
        self.v1DatabaseFileSelector.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.v1DatabaseFileSelector)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(DbConvert_V1ToV4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.v4DatabaseFileSelector = FileSelector(DbConvert_V1ToV4)
        self.v4DatabaseFileSelector.setObjectName(u"v4DatabaseFileSelector")
        sizePolicy.setHeightForWidth(self.v4DatabaseFileSelector.sizePolicy().hasHeightForWidth())
        self.v4DatabaseFileSelector.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.v4DatabaseFileSelector)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(DbConvert_V1ToV4)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.setDateNoneCheckBox = QCheckBox(self.groupBox)
        self.setDateNoneCheckBox.setObjectName(u"setDateNoneCheckBox")
        self.setDateNoneCheckBox.setChecked(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.setDateNoneCheckBox)

        self.commentTextEdit = QPlainTextEdit(self.groupBox)
        self.commentTextEdit.setObjectName(u"commentTextEdit")
        self.commentTextEdit.setEnabled(False)
        self.commentTextEdit.setPlainText(u"From V1 database")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.commentTextEdit)

        self.commentCheckBox = QCheckBox(self.groupBox)
        self.commentCheckBox.setObjectName(u"commentCheckBox")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.commentCheckBox)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.widget_3 = QWidget(DbConvert_V1ToV4)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.previewButton = QPushButton(self.widget_3)
        self.previewButton.setObjectName(u"previewButton")

        self.verticalLayout.addWidget(self.previewButton)

        self.transferButton = QPushButton(self.widget_3)
        self.transferButton.setObjectName(u"transferButton")
        font = QFont()
        font.setBold(True)
        self.transferButton.setFont(font)

        self.verticalLayout.addWidget(self.transferButton)


        self.horizontalLayout_3.addWidget(self.widget_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(DbConvert_V1ToV4)
        self.commentCheckBox.toggled.connect(self.commentTextEdit.setEnabled)

        QMetaObject.connectSlotsByName(DbConvert_V1ToV4)
    # setupUi

    def retranslateUi(self, DbConvert_V1ToV4):
        self.label.setText(QCoreApplication.translate("DbConvert_V1ToV4", u"V1 Database", None))
        self.label_2.setText(QCoreApplication.translate("DbConvert_V1ToV4", u"V4 Database", None))
        self.groupBox.setTitle(QCoreApplication.translate("DbConvert_V1ToV4", u"Options", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("DbConvert_V1ToV4", u"For V1 database, you cannot set the \"date\" property of a project to \"None\".\n"
"Thus, by default, GUI before v0.3.0 would set the date value to 2017/1/23.\n"
"Check this option to treat dates before 2017/1/23 as \"None\".", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(QCoreApplication.translate("DbConvert_V1ToV4", u"For V1 database, you cannot set the \"date\" property<br>\n"
"of a project to \"None\". Thus, the default GUI would<br>\n"
"set the default value to 2017/1/23.<br>\n"
"Check this option to treat dates before 2017/1/23<br>\n"
"to \"None\".<br>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("DbConvert_V1ToV4", u"Set date before<br>2017/1/23<br>to None", None))
        self.setDateNoneCheckBox.setText("")
        self.commentCheckBox.setText(QCoreApplication.translate("DbConvert_V1ToV4", u"Comment", None))
        self.previewButton.setText(QCoreApplication.translate("DbConvert_V1ToV4", u"Preview", None))
        self.transferButton.setText(QCoreApplication.translate("DbConvert_V1ToV4", u"Transfer", None))
        pass
    # retranslateUi

