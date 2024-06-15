# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceuGyqSf.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
from . import  icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1143, 777)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color:transparent;\n"
"background:transparent;\n"
"padding:0;\n"
"margin:0;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"#centralwidget,#mainBodyContent,#homeBtn,QLineEdit,QDateEdit,QPushButton,Line,QComboBox,QSpinBox{\n"
"background-color: #1b1b27\n"
"}\n"
"\n"
"#header, #mainBody, #footer{\n"
"background-color: #27263c\n"
"}\n"
"\n"
"#pushButton_3{\n"
"border:1px solid #cc5bce;\n"
"border-radius:19px;\n"
"text-align:center;\n"
"}\n"
"\n"
"#addUserBtn{\n"
"background-color: #cc5bce;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QPushButton,#leftMenu{\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius: 0;\n"
"border-bottom-right-radius: 0;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"#homeBtn{\n"
"border-left: 3px solid #cc5bce;\n"
"}\n"
"\n"
"QLineEdit,QDateEdit,QComboBox,QSpinBox{\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 50)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"#header, #mainBody{\n"
"background-color: #27263c;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.menuBtn.setFont(font)
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/align-justify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.menuBtn, 0, Qt.AlignmentFlag.AlignLeft)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"#label{\n"
"color:#ffffff;\n"
"font-family:\"Poppins\", sans-serif\n"
"}")

        self.horizontalLayout_4.addWidget(self.label, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/bell.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/activity.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"#pushButton_3{\n"
"				color:\"#FFFFFF\";\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.pushButton_3)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.mainBody.setMinimumSize(QSize(980, 625))
        self.mainBody.setStyleSheet(u"#mainBody{\n"
"background-color: #27263c;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.mainBody)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.leftMenu = QCustomSlideMenu(self.mainBody)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(0, 0))
        self.leftMenu.setMaximumSize(QSize(0, 16777215))
        self.leftMenu.setStyleSheet(u"#leftMenu{\n"
"background-color: #27263c;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 20)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 596))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.homeBtn = QPushButton(self.frame_3)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon5)

        self.verticalLayout_5.addWidget(self.homeBtn)

        self.reportsBtn = QPushButton(self.frame_3)
        self.reportsBtn.setObjectName(u"reportsBtn")
        self.reportsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/material_design/icons/material_design/print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reportsBtn.setIcon(icon6)

        self.verticalLayout_5.addWidget(self.reportsBtn)

        self.accountBtn = QPushButton(self.frame_3)
        self.accountBtn.setObjectName(u"accountBtn")
        self.accountBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.accountBtn.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.accountBtn)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.settingsBtn = QPushButton(self.frame_4)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon7)

        self.verticalLayout_6.addWidget(self.settingsBtn)

        self.helpBtn = QPushButton(self.frame_4)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/help-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon8)

        self.verticalLayout_6.addWidget(self.helpBtn)

        self.aboutBtn = QPushButton(self.frame_4)
        self.aboutBtn.setObjectName(u"aboutBtn")
        self.aboutBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/feather/icons/feather/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutBtn.setIcon(icon9)

        self.verticalLayout_6.addWidget(self.aboutBtn)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.leftMenu)

        self.mainBodyContent = QWidget(self.mainBody)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainPages = QCustomQStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_10 = QVBoxLayout(self.homePage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_3 = QWidget(self.homePage)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_6 = QFrame(self.widget_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(17)
        self.label_4.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.showUserFormBtn = QPushButton(self.frame_6)
        self.showUserFormBtn.setObjectName(u"showUserFormBtn")
        self.showUserFormBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/font_awesome/regular/icons/font_awesome/regular/square-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showUserFormBtn.setIcon(icon10)
        self.showUserFormBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.showUserFormBtn, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_6)

        self.tableWidgetUsers = QTableWidget(self.widget_3)
        self.tableWidgetUsers.setObjectName(u"tableWidgetUsers")
        self.tableWidgetUsers.setStyleSheet(u"QPushButton{\n"
"background-color: #cc5bce;\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"\n"
"}")
        self.tableWidgetUsers.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableWidgetUsers.setLineWidth(1)
        self.tableWidgetUsers.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidgetUsers.setSortingEnabled(True)
        self.tableWidgetUsers.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetUsers.horizontalHeader().setDefaultSectionSize(140)

        self.verticalLayout_11.addWidget(self.tableWidgetUsers)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.mainPages.addWidget(self.homePage)
        self.accountPage = QWidget()
        self.accountPage.setObjectName(u"accountPage")
        self.label_3 = QLabel(self.accountPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 146, 191, 71))
        self.label_3.setFont(font2)
        self.mainPages.addWidget(self.accountPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.label_5 = QLabel(self.settingsPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 150, 191, 81))
        self.label_5.setFont(font2)
        self.mainPages.addWidget(self.settingsPage)

        self.verticalLayout_2.addWidget(self.mainPages)


        self.horizontalLayout_2.addWidget(self.mainBodyContent)

        self.rightMenu = QCustomSlideMenu(self.mainBody)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(350, 0))
        self.rightMenu.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_2 = QWidget(self.rightMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(300, 247))
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"QPushButton {\n"
"background-color: #1b1b27;\n"
"border-radius: 10px;\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.closeRightMenu = QPushButton(self.widget_4)
        self.closeRightMenu.setObjectName(u"closeRightMenu")
        icon11 = QIcon()
        icon11.addFile(u":/feather/icons/feather/chevrons-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeRightMenu.setIcon(icon11)
        self.closeRightMenu.setIconSize(QSize(18, 18))

        self.horizontalLayout_8.addWidget(self.closeRightMenu, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addWidget(self.widget_4)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 70))
        self.label_2.setMaximumSize(QSize(70, 70))
        self.label_2.setPixmap(QPixmap(u":/feather/icons/feather/edit.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)

        self.verticalLayout_8.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QPushButton{\n"
"padding: 5px 10px;\n"
"border-radius: 5px;\n"
"background-color: #1b1b27\n"
"}")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.firstName = QLineEdit(self.frame_5)
        self.firstName.setObjectName(u"firstName")
        self.firstName.setReadOnly(False)

        self.verticalLayout_9.addWidget(self.firstName)

        self.lastName = QLineEdit(self.frame_5)
        self.lastName.setObjectName(u"lastName")

        self.verticalLayout_9.addWidget(self.lastName)

        self.email = QLineEdit(self.frame_5)
        self.email.setObjectName(u"email")

        self.verticalLayout_9.addWidget(self.email)

        self.phoneNb = QLineEdit(self.frame_5)
        self.phoneNb.setObjectName(u"phoneNb")

        self.verticalLayout_9.addWidget(self.phoneNb)

        self.address = QLineEdit(self.frame_5)
        self.address.setObjectName(u"address")

        self.verticalLayout_9.addWidget(self.address)

        self.birthDate = QDateEdit(self.frame_5)
        self.birthDate.setObjectName(u"birthDate")
        self.birthDate.setCalendarPopup(True)

        self.verticalLayout_9.addWidget(self.birthDate)

        self.imageFrame = QFrame(self.frame_5)
        self.imageFrame.setObjectName(u"imageFrame")
        self.imageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.imageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.imageFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.imageBtn = QPushButton(self.imageFrame)
        self.imageBtn.setObjectName(u"imageBtn")
        self.imageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/feather/icons/feather/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.imageBtn.setIcon(icon12)

        self.horizontalLayout_7.addWidget(self.imageBtn)

        self.imageLabel = QLabel(self.imageFrame)
        self.imageLabel.setObjectName(u"imageLabel")

        self.horizontalLayout_7.addWidget(self.imageLabel)


        self.verticalLayout_9.addWidget(self.imageFrame)

        self.subLine = QFrame(self.frame_5)
        self.subLine.setObjectName(u"subLine")
        self.subLine.setFrameShape(QFrame.Shape.HLine)
        self.subLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.subLine)

        self.subType = QComboBox(self.frame_5)
        icon13 = QIcon(QIcon.fromTheme(u"#000000"))
        self.subType.addItem(icon13, "")
        self.subType.addItem("")
        self.subType.addItem("")
        self.subType.addItem("")
        self.subType.addItem("")
        self.subType.setObjectName(u"subType")

        self.verticalLayout_9.addWidget(self.subType)

        self.subDurationW = QWidget(self.frame_5)
        self.subDurationW.setObjectName(u"subDurationW")
        self.horizontalLayout_10 = QHBoxLayout(self.subDurationW)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.subDurationW)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.subDuration = QSpinBox(self.subDurationW)
        self.subDuration.setObjectName(u"subDuration")

        self.horizontalLayout_10.addWidget(self.subDuration)


        self.verticalLayout_9.addWidget(self.subDurationW)

        self.widget_5 = QWidget(self.frame_5)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.labeldate = QLabel(self.widget_5)
        self.labeldate.setObjectName(u"labeldate")

        self.horizontalLayout_9.addWidget(self.labeldate)

        self.startDate = QDateEdit(self.widget_5)
        self.startDate.setObjectName(u"startDate")
        self.startDate.setCalendarPopup(True)

        self.horizontalLayout_9.addWidget(self.startDate)


        self.verticalLayout_9.addWidget(self.widget_5)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.addUserBtn = QPushButton(self.widget_2)
        self.addUserBtn.setObjectName(u"addUserBtn")
        self.addUserBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/feather/icons/feather/file-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addUserBtn.setIcon(icon14)
        self.addUserBtn.setIconSize(QSize(20, 20))
        self.addUserBtn.setCheckable(True)

        self.verticalLayout_8.addWidget(self.addUserBtn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_7.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.controlErrorsUser = QLabel(self.rightMenu)
        self.controlErrorsUser.setObjectName(u"controlErrorsUser")
        self.controlErrorsUser.setStyleSheet(u"#controlErrorsUser{\n"
"  text-align:center\n"
"}")
        self.controlErrorsUser.setScaledContents(True)
        self.controlErrorsUser.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.controlErrorsUser.setIndent(-1)
        self.controlErrorsUser.setOpenExternalLinks(False)

        self.verticalLayout_7.addWidget(self.controlErrorsUser)


        self.horizontalLayout_2.addWidget(self.rightMenu)


        self.verticalLayout.addWidget(self.mainBody)

        self.footer = QWidget(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.footer)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.pushButton_4.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.reportsBtn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.accountBtn.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings ", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.aboutBtn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Les Membres", None))
        self.showUserFormBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter Utilisateur", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Account Page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"settings Page", None))
        self.closeRightMenu.setText(QCoreApplication.translate("MainWindow", u"Fermer", None))
        self.label_2.setText("")
        self.firstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prenom", None))
        self.lastName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.phoneNb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numero Telephone", None))
        self.address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Adresse", None))
        self.birthDate.setSpecialValueText("")
        self.imageBtn.setText(QCoreApplication.translate("MainWindow", u"Choisir Image", None))
        self.imageLabel.setText("")
        self.subType.setItemText(0, QCoreApplication.translate("MainWindow", u"Abonnement mensuel", None))
        self.subType.setItemText(1, QCoreApplication.translate("MainWindow", u"Abonnement trimestriel", None))
        self.subType.setItemText(2, QCoreApplication.translate("MainWindow", u"Abonnement semestriel", None))
        self.subType.setItemText(3, QCoreApplication.translate("MainWindow", u"Abonnement annuel", None))
        self.subType.setItemText(4, QCoreApplication.translate("MainWindow", u"Autre", None))

        self.subType.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type d'abonnement", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Dur\u00e9e en mois :", None))
        self.labeldate.setText(QCoreApplication.translate("MainWindow", u"Date de d\u00e9but :", None))
        self.addUserBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter un membre", None))
        self.controlErrorsUser.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Copyright 2024", None))
    # retranslateUi

