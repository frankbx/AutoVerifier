#! /usr/bin/env python
# -*- coding: utf-8 -*-
from AutoTesterUI import AutoTesterFrm
from SerialHelper import SerialHelper
import wx
import binascii
import datetime
import logging
import platform
import threading
import Tkinter as tk
import ttk
import SerialTool

if platform.system() == "Windows":
    from  serial.tools import list_ports
elif platform.system() == "Linux":
    import glob, os, re

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')


class AutoTester(AutoTesterFrm):
    def __init__(self):
        AutoTesterFrm.__init__(self, None)
        self.ser_helper = SerialHelper()
        self.com_ports = list()
        self.thread_findserial = None
        self.find_all_serial_ports()

    '''
        Get all Serial Ports
    '''

    def find_all_serial_ports(self):

        if platform.system() == "Windows":
            try:
                self.temp_serial = list()
                for com in list_ports.comports():
                    # TODO check encoding correctness on Non-Chinese Windows
                    strCom = com[0] + ": " + com[1][:-7].decode("gbk").encode("utf-8")
                    self.temp_serial.append(strCom)
                for item in self.temp_serial:
                    if item not in self.com_ports:
                        self.ports_list.Append(item)
                for item in self.com_ports:
                    if item not in self.temp_serial:
                        self.ports_list.Delete(item)

                self.com_ports = self.temp_serial

                self.thread_findserial = threading.Timer(1, self.find_all_serial_ports)
                self.thread_findserial.setDaemon(True)
                self.thread_findserial.start()
            except Exception as e:
                logging.error(e)
        elif platform.system() == "Linux":
            # No Linux system supported so far
            pass


if __name__ == '__main__':
    app = wx.App()
    frm = AutoTester()
    frm.Show(True)
    app.MainLoop()
