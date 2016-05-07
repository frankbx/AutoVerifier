#! /usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Frank Bao"
__version__ = "v1.0"

import binascii
import logging

import serial


class SerialHelper(object):
    def __init__(self, Port="COM1", BaudRate="19200", ByteSize="8", Parity="N", Stopbits="1"):
        '''
        初始化一些参数
        '''
        self.l_serial = None
        self.alive = False
        self.port = Port
        self.baudrate = BaudRate
        self.bytesize = ByteSize
        self.parity = Parity
        self.stopbits = Stopbits
        self.thresholdValue = 64
        self.receive_data = ""

    def start(self):
        self.l_serial = serial.Serial()
        self.l_serial.port = self.port
        self.l_serial.baudrate = self.baudrate
        self.l_serial.bytesize = int(self.bytesize)
        self.l_serial.parity = self.parity
        self.l_serial.stopbits = int(self.stopbits)
        self.l_serial.timeout = 2

        try:
            self.l_serial.open()
            if self.l_serial.isOpen():
                self.alive = True
        except Exception as e:
            self.alive = False
            logging.error(e)

    def stop(self):
        self.alive = False
        if self.l_serial.isOpen():
            self.l_serial.close()

    def write(self, data, isRecording=False):
        if self.alive:
            if self.l_serial.isOpen():
                if isRecording:
                    data = binascii.unhexlify(data)
                self.l_serial.write(data)
                print (data)


if __name__ == '__main__':
    import threading

    ser = SerialHelper()
    ser.start()

    ser.write("123", isHex=False)
    thread_read = threading.Thread(target=ser.read)
    thread_read.setDaemon(True)
    thread_read.start()
    import time

    time.sleep(5)
    ser.stop()
