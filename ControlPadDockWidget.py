#! /usr/bin/env python
# coding=utf-8
import sys

import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


# TODO Disable key pad if not connected to a Serial Port
# TODO add code to send key to serial port
# TODO add code to record script to scripting window
# TODO add play function, play the script showing in scripting window
class ControlPadDockWidget(QDockWidget):
    def __init__(self, parent=None):
        super(ControlPadDockWidget, self).__init__("Control Pad", parent)
        self.setObjectName('ControlPadDockWidget')
        self.setAllowedAreas(Qt.RightDockWidgetArea)
        controlPadWidget = QWidget()
        vbox = QVBoxLayout()
        controlPadWidget.setLayout(vbox)
        self.initQuickKeyPad()
        self.initControlPad()
        vbox.addWidget(self.quickKeyPadWidget)
        vbox.addWidget(self.controlPadWidget)
        self.setWidget(controlPadWidget)

    def initQuickKeyPad(self):
        self.quickKeyPadWidget = QWidget()
        grid = QGridLayout()
        # TODO Fill in proper names instead of placeholder
        names = ['A', 'V', 'C', 'D', 'E', 'F', '/',
                 '4', '5', '6', '#', '1', '2', '3', '-', '0',
                 '.', '=', '+', 'K']
        pos = [
            (0, 0), (0, 1), (0, 2), (0, 3),
            (1, 0), (1, 1), (1, 2), (1, 3),
            (2, 0), (2, 1), (2, 2), (2, 3),
            (3, 0), (3, 1), (3, 2), (3, 3),
            (4, 0), (4, 1), (4, 2), (4, 3)
        ]
        j = 0
        for i in names:
            button = QPushButton(i)
            grid.addWidget(button, pos[j][0], pos[j][1])
            # TODO add connection to actions
            j = j + 1
        self.quickKeyPadWidget.setLayout(grid)

    def initControlPad(self):
        self.controlPadWidget = QWidget()
        vbox = QVBoxLayout()
        self.controlPadWidget.setLayout(vbox)
        self.recordButton = QPushButton("Record")
        self.playButton = QPushButton("Play")
        vbox.addWidget(self.recordButton)
        vbox.addWidget(self.playButton)


if __name__ == '__main__':
    print(PYQT_VERSION_STR)
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainWindow = QMainWindow()
    mainWindow.setCentralWidget(QWidget())
    controlPadDockWidget = ControlPadDockWidget()
    mainWindow.addDockWidget(Qt.RightDockWidgetArea, controlPadDockWidget)
    mainWindow.setFixedSize(1024, 768)
    mainWindow.show()
    sys.exit(app.exec_())
