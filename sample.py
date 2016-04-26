#!/usr/bin/env python
# encoding: utf-8

import time

from PIL import Image
from pylab import *

from AbbyyOnlineSdk import *
import OCRProcessor

img = Image.open('1.bmp')
processor = AbbyyOnlineSdk()
# print "Using proxy at %s" % proxyString
processor.Proxy = urllib2.ProxyHandler({"http": '3.20.128.6:88'})


def show_pic(img):
    im = array(img)
    imshow(im)
    show()


# Recognize a file at filePath and save result to resultFilePath
def recognizeFile(filePath, resultFilePath, language, outputFormat):
    print "Uploading.."
    settings = ProcessingSettings()
    settings.Language = language
    settings.OutputFormat = outputFormat
    task = processor.ProcessImage(filePath, settings)
    if task == None:
        print "Error"
        return
    print "Id = %s" % task.Id
    print "Status = %s" % task.Status

    # Wait for the task to be completed
    sys.stdout.write("Waiting..")
    # Note: it's recommended that your application waits at least 2 seconds
    # before making the first getTaskStatus request and also between such requests
    # for the same task. Making requests more often will not improve your
    # application performance.
    # Note: if your application queues several files and waits for them
    # it's recommended that you use listFinishedTasks instead (which is described
    # at http://ocrsdk.com/documentation/apireference/listFinishedTasks/).

    while task.IsActive() is True:
        time.sleep(2)
        sys.stdout.write(".")
        task = processor.GetTaskStatus(task)

    print "Status = %s" % task.Status

    if task.Status == "Completed":
        if task.DownloadUrl is not None:
            result = processor.DownloadResult(task, resultFilePath)
            print "Result was written to %s" % resultFilePath
    else:
        print "Error processing task"

    return result


def ocr(img, box=None, filename=None):
    figure()
    gray()
    if box is not None:
        p = img.crop(box)
        show_pic(p)
        p.save(filename + '.bmp', 'bmp')
        recognizeFile(filename + '.bmp', filename + '.txt', 'English', 'txt')
    else:
        pass


# # string "perform....."
# box = (841, 381, 1417, 677)
#
# ocr(img, box, 'perform1')
#
# box = (713, 1009, 1113, 1165)
# ocr(img, box, 'perform2')
# Not Tested
# box = (435, 385, 512, 403)
# ocr(img, box, 'nottested')
# # button "Ventilator Leak"
# box = (939, 212, 1006, 253)
# ocr(img, box, 'ventilatorleak')
# # alarm slot
# box = (703, 21, 795, 76)
# ocr(img, box, 'alarm')
# # # 24-Nov-2015 19:52
box = (410, 358, 536, 376)
ocr(img, box, 'testtime')
# box = (583,125,860,260)
# ocr(img, box, 'testtime1')
# box = (963,1301,1769,1357)
# ocr(img, box, 'testtime2')
