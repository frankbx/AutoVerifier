#! /usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import platform

import wx

from AutoTesterUI import AutoTesterFrm
from SerialHelper import SerialHelper
from ScriptHelper import ScriptHelper

if platform.system() == "Windows":
    from  serial.tools import list_ports
elif platform.system() == "Linux":
    pass

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')
VK_DOWN = chr(0xd6)
VK_UP = chr(0xd5)
VK_RETURN = chr(13)


class AutoTester(AutoTesterFrm):
    def __init__(self):
        AutoTesterFrm.__init__(self, None)
        self.serial_helper = None
        self.script_helper = None
        self.com_ports = list()
        self.find_all_serial_ports()
        self.Layout()
        self.is_recording = False
        self.action_sequence = None

    '''
        Get all Serial Ports
    '''

    def find_all_serial_ports(self):

        if platform.system() == "Windows":
            try:
                self.com_ports = list()
                self.ports_list.Clear()
                for com in list_ports.comports():
                    strCom = com[0]
                    # self.com_ports.append(strCom)
                    self.com_ports.append(strCom)
                for item in self.com_ports:
                    self.ports_list.Append(item)
                if len(self.com_ports) >= 1:
                    self.ports_list.SetStringSelection(self.com_ports[0])

            except Exception as e:
                logging.error(e)
        elif platform.system() == "Linux":
            # No Linux system supported so far
            pass

    def open(self, event):
        self.toggle()

    def send_key(self, event):
        if self.script_helper is None:
            self.script_helper = ScriptHelper("script.txt")
        if self.serial_helper is None:
            self.toggle()
        btn = event.GetEventObject().GetLabelText()
        key = self.button_to_key_press(btn)
        self.serial_helper.write(key)
        if self.is_recording == True:
            self.script_helper.write(key + '\n')

    def button_to_key_press(self, btn):
        if btn == 'Wheel Right':
            return VK_UP
        elif btn == 'Wheel Left':
            return VK_DOWN
        elif btn == 'Confirm':
            return VK_RETURN
        elif btn == 'Vent Modes':
            return 'v'
        elif btn == 'Alarm Setup':
            return 'a'

    def toggle(self):
        '''
        Open/Close the selected Serial Port and change the button appearance accordingly.
        '''
        if self.tgl_btn_open.GetLabelText() == "Open":
            try:
                self.port = self.ports_list.GetStringSelection()
                self.baudrate = self.baudrate_list.GetStringSelection()
                self.parity = self.parity_list.GetStringSelection()
                self.databit = self.databit_list.GetStringSelection()
                self.stopbit = self.stopbit_list.GetStringSelection()
                print self.port, self.baudrate, self.parity, self.databit, self.stopbit
                self.serial_helper = SerialHelper(Port=self.port,
                                                  BaudRate=self.baudrate,
                                                  ByteSize=self.databit,
                                                  Parity=self.parity,
                                                  Stopbits=self.stopbit)
                self.serial_helper.start()
                self.tgl_btn_open.SetLabelText("Close")
                self.tgl_btn_open.SetBackgroundColour("Blue")
                self.tgl_btn_open.SetForegroundColour("White")
                self.status_bar.SetStatusText((self.port + " has been opened Successfully!"), 0)
            except Exception as e:
                logging.error(e)

        elif self.tgl_btn_open.GetLabelText() == "Close":
            try:
                self.serial_helper.stop()
            except Exception as e:
                logging.error(e)
            self.tgl_btn_open.SetLabelText("Open")
            self.tgl_btn_open.SetBackgroundColour(None)
            self.tgl_btn_open.SetForegroundColour(None)
            self.status_bar.SetStatusText((self.port + " has been closed Successfully!"), 0)

    def recording(self, event):
        if self.script_helper is None:
            self.script_helper = ScriptHelper("script.txt")
        if self.serial_helper is None:
            self.toggle()
        if self.tgl_btn_recording.GetLabelText() == "Record":
            self.is_recording = True
            self.action_sequence = list()
            self.script_helper = ScriptHelper("script.txt")
            self.tgl_btn_recording.SetLabelText("Recording...")
            self.tgl_btn_recording.SetBackgroundColour('Red')
            self.tgl_btn_recording.SetForegroundColour('White')
            self.status_bar.SetStatusText("Recording started.")
        elif self.tgl_btn_recording.GetLabelText() == "Recording...":
            self.tgl_btn_recording.SetLabelText("Record")
            self.is_recording = False
            self.script_helper.close()
            self.tgl_btn_recording.SetBackgroundColour(None)
            self.tgl_btn_recording.SetForegroundColour(None)
            self.status_bar.SetStatusText("Recording ended.")

    def play(self, event):
        # if self.script_helper is None:
        self.script_helper = ScriptHelper("script.txt", 'r')
        if self.serial_helper is None:
            self.toggle()
        print self.serial_helper
        for line in self.script_helper.readlines():
            # print line[:-1]
            import time
            time.sleep(1)
            self.serial_helper.write(line)


if __name__ == '__main__':
    app = wx.App()
    frm = AutoTester()
    frm.Show(True)
    app.MainLoop()
