#! /usr/bin/env python
# coding=utf-8
import logging
import platform
import sys

import psutil
import qdarkstyle
from PyQt4.QtCore import *
from PyQt4.QtGui import *

if platform.system() == "Windows":
    from  serial.tools import list_ports
elif platform.system() == "Linux":
    pass
EVENT_TIMER = 'eTimer'


class AutoTesterMainWindow(QMainWindow):
    def __init__(self):
        super(AutoTesterMainWindow, self).__init__()
        self.setWindowTitle('Auto Tester')
        self.initUI()
        self.initMenu()
        self.initStatusBar()

    def initUI(self):
        # -----------------------------------------------------------------------------------------
        # initialize central widget
        self.imageLabel = QLabel()
        self.imageLabel.setMinimumSize(200, 200)
        self.imageLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.setCentralWidget(self.imageLabel)

        # -------------------------------------------------------------------------------------------
        # initialize DockWidget to contain SerialPortWidget
        serialPortDockWidget = QDockWidget('Serial Port', self)
        serialPortDockWidget.setObjectName('SerialPortDockWidget')
        serialPortDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        # -----------------------------------------------------------------------------------------
        # initialize widget contains list of serial ports and serial port settings
        serialPortWidget = QWidget()
        self.serialPortCombo = QComboBox()
        self.fill_in_all_serial_ports(self.serialPortCombo)
        serialPortLayout = QGridLayout()
        serialPortLayout.addWidget(self.serialPortCombo, 0, 0)
        serialPortWidget.setLayout(serialPortLayout)
        serialPortWidget.setGeometry(300,300,300,200)


        serialPortDockWidget.setWidget(serialPortWidget)


        self.addDockWidget(Qt.LeftDockWidgetArea, serialPortDockWidget)

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
        return 'CPU使用率：%d%%   内存使用率：%d%%' % (cpuPercent, memoryPercent)

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

    def fill_in_all_serial_ports(self, widget):
        if platform.system() == "Windows":
            try:
                self.com_ports = list()
                # self.ports_list.Clear()
                for com in list_ports.comports():
                    strCom = com[0]
                    self.com_ports.append(strCom)
                for item in self.com_ports:
                    widget.addItem(item)
                if len(self.com_ports) >= 1:
                    pass

            except Exception as e:
                logging.error(e)
        elif platform.system() == "Linux":
            # No Linux system supported so far
            pass


class AboutWidget(QDialog):
    # ----------------------------------------------------------------------
    def __init__(self, parent=None):
        super(AboutWidget, self).__init__(parent)

        self.initUi()

    # ----------------------------------------------------------------------
    def initUi(self):
        self.setWindowTitle('About Tester')

        text = u"""
            Developed by testers, for tester.
            """

        label = QLabel()
        label.setText(text)
        label.setMinimumWidth(500)

        vbox = QVBoxLayout()
        vbox.addWidget(label)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
    mainWindow = AutoTesterMainWindow()
    mainWindow.showMaximized()
    sys.exit(app.exec_())
