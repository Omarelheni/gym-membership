########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys

from operations.main_ui_functions import AllUiFunctions
########################################################################
# IMPORT GUI FILE
from src.ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
########################################################################

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow, AllUiFunctions):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        # Use this if you only have one json file named "style.json" inside the root directory, "json" directory or "jsonstyles" folder.
        # loadJsonStyle(self, self.ui)

        # Use this to specify your json file(s) path/name
        loadJsonStyle(self, self.ui, jsonFiles={
            "json-styles/style.json"
        })

        ########################################################################

        #######################################################################
        # REMOVE TITLE BAR
        #######################################################################
        self.setWindowFlags(Qt.FramelessWindowHint)

        #######################################################################
        # CONNECT BUTTON SIGNALS TO SLOTS
        #######################################################################
        self.ui.closeAppBtn.clicked.connect(self.close_app)
        self.ui.maximizeRestoreAppBtn.clicked.connect(self.maximize_restore_app)
        self.ui.minimizeAppBtn.clicked.connect(self.minimize_app)

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()

        ########################################################################
        # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET
        # ITS IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
        # THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
        # TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
        ########################################################################
        # self = QMainWindow class
        QAppSettings.updateAppSettings(self)
        self.set_main_ui_functions()

        ########################################################################
        # CUSTOM TITLE BAR FUNCTIONALITY
        ########################################################################
        self.oldPos = None

    ########################################################################
    # SLOT FUNCTIONS FOR BUTTONS
    ########################################################################
    def close_app(self):
        self.close()

    def maximize_restore_app(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def minimize_app(self):
        self.showMinimized()

    ########################################################################
    # MOUSE EVENTS FOR MOVING WINDOW
    ########################################################################
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
            event.accept()

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ##
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())