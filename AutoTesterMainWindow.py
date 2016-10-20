#! /usr/bin/env python
# coding=utf-8

import sys

import psutil
import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ControlPadDockWidget import ControlPadDockWidget
from ScriptDockWidget import ScriptDockWidget
from SerialPortDockWidget import SerialPortDockWidget


class AutoTesterMainWindow(QMainWindow):
    def __init__(self):
        super(AutoTesterMainWindow, self).__init__()
        self.setWindowTitle('Automation')
        self.initCentralWidget()
        self.setCentralWidget(self.centralWidget)
        self.initMenu()
        self.initStatusBar()
        self.serialPortDockWidget = SerialPortDockWidget(self)
        self.addDockWidget(Qt.RightDockWidgetArea, self.serialPortDockWidget)  # ,Qt.BottomRightCorner)
        self.controlPadDockWidget = ControlPadDockWidget(self)
        self.addDockWidget(Qt.RightDockWidgetArea, self.controlPadDockWidget)
        self.scriptDockWidget = ScriptDockWidget(self)
        self.addDockWidget(Qt.RightDockWidgetArea, self.scriptDockWidget)  # ,Qt.TopRightCorner)
        self.tabifyDockWidget(self.controlPadDockWidget, self.serialPortDockWidget)

    def initCentralWidget(self):
        self.centralWidget = QWidget()
        self.centralWidget.setFixedSize(1024, 768)

    def initMenu(self):
        menubar = self.menuBar()
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)
        aboutAction = QAction('About', self)
        aboutAction.triggered.connect(self.openAbout)
        sysMenu = menubar.addMenu('System')
        sysMenu.addAction(exitAction)
        # functionMenu = menubar.addMenu('Function')
        helpMenu = menubar.addMenu('Help')
        helpMenu.addAction(aboutAction)

    def initStatusBar(self):
        self.statusLabel = QLabel()
        self.statusLabel.setAlignment(Qt.AlignLeft)
        status = self.statusBar()
        status.addPermanentWidget(self.statusLabel)
        self.statusLabel.setText(self.getCpuMemory())
        status.showMessage('Ready', 5000)
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateStatusBar)
        self.timer.start(1000)

    def updateStatusBar(self):
        self.statusLabel.setText(self.getCpuMemory())

    def getCpuMemory(self):
        cpuPercent = psutil.cpu_percent()
        memoryPercent = psutil.virtual_memory().percent
        return 'CPU Usage：%d%%   Memory Usage：%d%%' % (cpuPercent, memoryPercent)

    def openAbout(self):
        aboutWidget = AboutWidget(self)
        aboutWidget.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit',
                                     'Are you sure to exit?', QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class AboutWidget(QDialog):
    # ----------------------------------------------------------------------
    def __init__(self, parent=None):
        super(AboutWidget, self).__init__(parent)
        self.initUi()

    # ----------------------------------------------------------------------
    def initUi(self):
        self.setWindowTitle('About Tester')
        text = """
            Developed by testers, for testers.
            """
        label = QLabel()
        label.setText(text)
        label.setMinimumWidth(500)

        vbox = QVBoxLayout()
        vbox.addWidget(label)

        self.setLayout(vbox)


if __name__ == '__main__':
    print(PYQT_VERSION_STR)
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainWindow = AutoTesterMainWindow()
    # mainWindow.setFixedSize(1024, 768)
    mainWindow.showMaximized()
    sys.exit(app.exec_())
