#! /usr/bin/env python
# coding=utf-8
import sys

import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import SerialHelper as sh


# TODO Disable key pad if not connected to a Serial Port
# TODO add code to send key to serial port
# TODO add code to record script to scripting window
# TODO add play function, play the script showing in scripting window
class ControlPadDockWidget(QDockWidget):
    def __init__(self, serialHelper=None,parent=None):
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
        self.serialHelper = serialHelper

    def initQuickKeyPad(self):
        self.quickKeyPadWidget = QWidget()
        grid = QGridLayout()

        self.alarmSettpingBtn = QPushButton("Alarm Setup")
        grid.addWidget(self.alarmSettpingBtn, 0, 0)
        self.alarmSettpingBtn.clicked.connect(lambda: self.sendKey(sh.VK_ALARM_SETUP))

        self.ventModeBtn = QPushButton("Vent Modes")
        grid.addWidget(self.ventModeBtn, 0, 1)
        self.ventModeBtn.clicked.connect(lambda: self.sendKey(sh.VK_VENT_MODES))

        self.wheelUpBtn = QPushButton("Up")
        grid.addWidget(self.wheelUpBtn, 1, 0)
        self.wheelUpBtn.clicked.connect(lambda: self.sendKey(sh.VK_UP))

        self.wheelDownBtn = QPushButton("Down")
        grid.addWidget(self.wheelDownBtn, 1, 1)
        self.wheelDownBtn.clicked.connect(lambda: self.sendKey(sh.VK_DOWN))

        self.returnBtn = QPushButton("Return")
        grid.addWidget(self.returnBtn, 2, 0)
        self.returnBtn.clicked.connect(lambda: self.sendKey(sh.VK_RETURN))

        self.quickKeyPadWidget.setLayout(grid)

    def initControlPad(self):
        self.controlPadWidget = QWidget()
        vbox = QVBoxLayout()
        self.controlPadWidget.setLayout(vbox)
        self.recordButton = QPushButton("Record")
        self.playButton = QPushButton("Play")
        vbox.addWidget(self.recordButton)
        vbox.addWidget(self.playButton)

    def sendKey(self, key):
        if self.parent().serialHelper is not None:
            print('key sent', key)


if __name__ == '__main__':
    print(PYQT_VERSION_STR)
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainWindow = QMainWindow()
    mainWindow.setCentralWidget(QWidget())
    controlPadDockWidget = ControlPadDockWidget(sh.SerialHelper())
    mainWindow.addDockWidget(Qt.RightDockWidgetArea, controlPadDockWidget)
    mainWindow.setFixedSize(1024, 768)
    mainWindow.show()
    sys.exit(app.exec_())
