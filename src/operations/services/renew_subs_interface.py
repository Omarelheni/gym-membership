# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'renew_subsVXNEOZ.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class RenewSubDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(429, 194)
        Dialog.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color:#27263c;\n"
"padding:0;\n"
"margin:0;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QDialog{\n"
"padding-top:20px;\n"
"}\n"
"\n"
"QLineEdit,QDateEdit,QComboBox,QSpinBox{\n"
"background-color: #1b1b27;\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.subType = QComboBox(self.widget)
        icon = QIcon(QIcon.fromTheme(u"#000000"))
        self.subType.addItem(icon, "")
        self.subType.addItem("")
        self.subType.addItem("")
        self.subType.addItem("")
        self.subType.addItem("")
        self.subType.setObjectName(u"subType")
        self.subType.currentIndexChanged.connect(self.on_combobox_type_change)

        self.verticalLayout_2.addWidget(self.subType)

        self.subDurationW = QWidget(self.widget)
        self.subDurationW.setObjectName(u"subDurationW")
        self.subDurationW.setHidden(True)
        self.horizontalLayout_10 = QHBoxLayout(self.subDurationW)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.subDurationW)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.subDuration = QSpinBox(self.subDurationW)
        self.subDuration.setObjectName(u"subDuration")

        self.horizontalLayout_10.addWidget(self.subDuration)


        self.verticalLayout_2.addWidget(self.subDurationW)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.labeldate = QLabel(self.widget_5)
        self.labeldate.setObjectName(u"labeldate")

        self.horizontalLayout_9.addWidget(self.labeldate)

        self.startDate = QDateEdit(self.widget_5)
        self.startDate.setObjectName(u"startDate")
        self.startDate.setCalendarPopup(True)
        self.startDate.setDate(QDate.currentDate())


        self.horizontalLayout_9.addWidget(self.startDate)


        self.verticalLayout_2.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Cancel)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.subType.setItemText(0, QCoreApplication.translate("Dialog", u"Abonnement mensuel", None))
        self.subType.setItemText(1, QCoreApplication.translate("Dialog", u"Abonnement trimestriel", None))
        self.subType.setItemText(2, QCoreApplication.translate("Dialog", u"Abonnement semestriel", None))
        self.subType.setItemText(3, QCoreApplication.translate("Dialog", u"Abonnement annuel", None))
        self.subType.setItemText(4, QCoreApplication.translate("Dialog", u"Autre", None))

        self.subType.setPlaceholderText(QCoreApplication.translate("Dialog", u"Type d'abonnement", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Dur\u00e9e en mois :", None))
        self.labeldate.setText(QCoreApplication.translate("Dialog", u"Date de d\u00e9but :", None))
    # retranslateUi

    def on_combobox_type_change(self):
        if self.subType.currentText() == "Autre":
            self.subDurationW.setHidden(False)
        else:
            self.subDurationW.setHidden(True)
