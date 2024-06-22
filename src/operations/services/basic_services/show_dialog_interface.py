# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledmJaVbI.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(484, 390)
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
        Dialog.setModal(False)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")


        self.verticalLayout.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi
    def addFieldToWidget(self,ui_name="",table_name="",value="",ui_label="",type="Text",widget=None):
        if type =="Text":
            label_ui_name = ui_name+'Label'
            text_ui_name = ui_name+'Text'
            widget_ui_name = table_name + 'Widget'
            horizontal_layout_ui_name = ui_name+ "HorizontalLayout"

            setattr(self,widget_ui_name,QWidget(self.widget))
            getattr(self,widget_ui_name).setObjectName(widget_ui_name)

            setattr(self, horizontal_layout_ui_name,QHBoxLayout(getattr(self,widget_ui_name)))
            getattr(self,horizontal_layout_ui_name).setObjectName(horizontal_layout_ui_name)

            setattr(self, label_ui_name,QLabel(getattr(self,widget_ui_name)))
            getattr(self,label_ui_name).setObjectName(label_ui_name)


            getattr(self,horizontal_layout_ui_name).addWidget(getattr(self,label_ui_name))

            setattr(self, text_ui_name,QLineEdit(getattr(self,widget_ui_name)))
            getattr(self,text_ui_name).setObjectName(text_ui_name)
            getattr(self,text_ui_name).setReadOnly(True)

            getattr(self,horizontal_layout_ui_name).addWidget(getattr(self,text_ui_name))

            self.verticalLayout_2.addWidget(getattr(self,widget_ui_name), 0, Qt.AlignmentFlag.AlignTop)

            getattr(self,label_ui_name).setText(QCoreApplication.translate("Dialog", ui_label, None))
            getattr(self,text_ui_name).setText(QCoreApplication.translate("Dialog", value, None))
        elif type=="Image":
            print('hey inn ')
            self.verticalLayout_2.addWidget(widget, 0, Qt.AlignmentFlag.AlignTop)



    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi

