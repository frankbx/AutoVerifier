#! /usr/bin/env python
# coding=utf-8
import sys

import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ScriptDockWidget(QDockWidget):
    def __init__(self, parent=None):
        super(ScriptDockWidget, self).__init__("Scripting", parent)
        self.setObjectName('ScriptDockWidget')
        self.setAllowedAreas(Qt.BottomDockWidgetArea | Qt.RightDockWidgetArea)

    '''Accept input to update the script accordingly'''

    # TODO add code to display corresponding script in the window
    def update_script(self, script):
        pass

    # TODO add Save Script function
    def save_script(self, filename):
        pass

    # TODO add load Script function
    def load_script(self, filename):
        pass

    # TODO add undo function in case user error
    def undo(self):
        pass


if __name__ == '__main__':
    print(PYQT_VERSION_STR)
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainWindow = QMainWindow()
    mainWindow.setCentralWidget(QWidget())
    scriptDockWidget = ScriptDockWidget()
    mainWindow.addDockWidget(Qt.BottomDockWidgetArea, scriptDockWidget)
    mainWindow.setFixedSize(1024, 768)
    mainWindow.show()
    sys.exit(app.exec_())
