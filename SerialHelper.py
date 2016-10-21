#! /usr/bin/env python
# -*- coding: utf-8 -*-
import binascii
import platform

import serial
from serial.tools import list_ports

''' Utility class to operate Serial Ports'''


class SerialHelper(object):
    def __init__(self):
        self.serial_port = None
        self.alive = False

    def start(self, port="COM1", baudrate="19200", bytesize="8", parity="N", stopbits="1"):
        self.serial_port = serial.Serial(port=port, baudrate=baudrate, bytesize=bytesize, parity=parity,
                                         stopbits=stopbits)

        self.serial_port.timeout = 2

        try:
            self.serial_port.open()
            if self.serial_port.isOpen():
                self.alive = True
        except Exception as e:
            self.alive = False
            print(e)

    def stop(self):
        if self.alive is True:
            self.alive = False
            if self.serial_port.isOpen():
                self.serial_port.close()

    def write(self, data, isRecording=False):
        if self.alive:
            if self.serial_port.isOpen():
                if isRecording:
                    data = binascii.unhexlify(data)
                # print(data.encode(encoding="utf-8"))
                # print(type(data.encode(encoding="utf-8")))
                self.serial_port.write(data.encode(encoding="utf-8"))
                # print(data)

    @staticmethod
    def get_all_serial_ports():
        com_ports = []
        if platform.system() == "Windows":

            try:
                for com in list_ports.comports():
                    strCom = com[0]
                    com_ports.append(strCom)
            except Exception as e:
                print(e)
        elif platform.system() == "Linux":
            # No Linux system supported so far
            pass
        return com_ports


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
