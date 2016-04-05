#! /usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Frank Bao"
__version__ = "v1.0"


class ScriptHelper(object):
    def __init__(self, filename=None, mode='a+'):
        self.script_file = None
        if filename is not None:
            self.script_file = open(filename, mode)
        else:
            self.script_file = open('script.txt', mode)

    def write(self, data):
        self.script_file.write(data)

    def readlines(self):
        return self.script_file.readlines()

    def readline(self):
        return self.script_file.readline()

    def close(self):
        if self.script_file is not None:
            self.script_file.close()
