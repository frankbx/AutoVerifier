#! /usr/bin/env python
# coding=utf-8

import sys

import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from SerialHelper import SerialHelper


class SerialPortDockWidget(QDockWidget):
    def __init__(self, serialHelper=None, parent=None):
        super(SerialPortDockWidget, self).__init__("Serial Port", parent)
        self.setObjectName('SerialPortDockWidget')
        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        # initialize widget contains list of serial ports and serial port settings
        serialPortWidget = QWidget()
        vbox = QVBoxLayout()
        serialPortWidget.setLayout(vbox)
        self.initSerialPortSettingWidget()
        self.initSerialPortControlWidget()
        vbox.addWidget(self.serialPortSettingWidget)
        vbox.addWidget(self.serialPortControlWidget)
        self.setWidget(serialPortWidget)
        self.setFixedSize(200, 300)
        self.com_ports = list()
        self.serialHelper = serialHelper

    def initSerialPortControlWidget(self):
        self.serialPortControlWidget = QWidget()
        vbox = QVBoxLayout()
        self.serialPortControlWidget.setLayout(vbox)
        self.openButton = QPushButton("Open")
        self.closeButton = QPushButton("Close")
        vbox.addWidget(self.openButton)
        vbox.addWidget(self.closeButton)
        self.closeButton.clicked.connect(self.close_port)
        self.openButton.clicked.connect(self.open_port)

    def initSerialPortSettingWidget(self):
        self.serialPortSettingWidget = QWidget()
        self.serialPortCombo = QComboBox()
        self.serialPortCombo.sizePolicy()
        self.com_ports = SerialHelper.get_all_serial_ports()
        # self.com_ports = self.ports
        for port in self.com_ports:
            self.serialPortCombo.addItem(port)
        serialPortLayout = QGridLayout()
        serialPortLayout.setSpacing(10)
        serialPortLayout.addWidget(self.serialPortCombo, 0, 0, 1, 2)
        self.serialPortSettingWidget.setLayout(serialPortLayout)
        baudrateLabel = QLabel('Baudrate')
        baudrate_list = [u"1200", u"2400", u"4800", u"9600", u"14400", u"19200", u"38400", u"43000", u"57600",
                         u"76800", u"115200", u"12800"]
        baudrateCombo = QComboBox()
        baudrateCombo.addItems(baudrate_list)
        # Set default baudrate to 19200
        baudrateCombo.setCurrentIndex(5)
        serialPortLayout.addWidget(baudrateLabel, 1, 0)
        serialPortLayout.addWidget(baudrateCombo, 1, 1)
        parity_list = [u"N", u"E", u"O", u"M", u"S"]
        parityLabel = QLabel('Parity')
        parityCombo = QComboBox()
        parityCombo.addItems(parity_list)
        serialPortLayout.addWidget(parityLabel, 2, 0)
        serialPortLayout.addWidget(parityCombo, 2, 1)
        databitLabel = QLabel('Databit')
        databit_list = [u"5", u"6", u"7", u"8"]
        databitCombo = QComboBox()
        databitCombo.addItems(databit_list)
        # Set default databit to 8
        databitCombo.setCurrentIndex(3)
        serialPortLayout.addWidget(databitLabel, 3, 0)
        serialPortLayout.addWidget(databitCombo, 3, 1)
        stopbitLabel = QLabel('Stopbit')
        stopbitCombo = QComboBox()
        stopbit_list = [u"1", u"1.5", u"2"]
        stopbitCombo.addItems(stopbit_list)
        serialPortLayout.addWidget(stopbitLabel, 4, 0)
        serialPortLayout.addWidget(stopbitCombo, 4, 1)

    def open_port(self):
        print("open button clicked")
        if self.serialHelper is None:
            port = self.serialPortCombo.currentText()
            print("port is", port)
            if port.startswith("COM"):
                self.serialHelper = SerialHelper(port=port)
                self.parent.serialHelper = self.serialHelper
                # print(port)
                # print(self.serialHelper.alive, self.serialHelper.serial_port.isOpen())
        if not self.serialHelper.alive:
            self.serialHelper.start()
            print(self.serialHelper.alive, self.serialHelper.serial_port.isOpen())


    # TODO disable close button if not serial port is open
    def close_port(self):
        print('close button clicked')
        if self.serialHelper is not None:
            if self.serialHelper.serial_port.isOpen():
                self.serialHelper.stop()
            else:
                print("No open port")


if __name__ == '__main__':
    print(PYQT_VERSION_STR)
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainWindow = QMainWindow()
    mainWindow.setCentralWidget(QWidget())
    controlPadDockWidget = SerialPortDockWidget()
    mainWindow.addDockWidget(Qt.LeftDockWidgetArea, controlPadDockWidget)
    mainWindow.setFixedSize(1024, 768)
    mainWindow.show()
    sys.exit(app.exec_())
