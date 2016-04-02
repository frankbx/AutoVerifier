#!/usr/bin/env python
# encoding: utf-8
import cv2
print cv2.__version__
capture = cv2.VideoCapture(0)
print capture.isOpened()
size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
video = cv2.VideoWriter("VideoTest.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), 1, size)
num = 0
# 要不断读取image需要设置一个循环
while True:
    ret, img = capture.read()
    # 视频中的图片一张张写入
    video.write(img)
    cv2.imshow('Video', img)
    key = cv2.waitKey(1)  # 里面数字为delay时间，如果大于0为刷新时间，
    # 超过指定时间则返回-1，等于0没有返回值,但也可以读取键盘数值，
    # cv2.imwrite('%s.jpg' % (str(num)), img)
    num = num + 1
    if key == ord('q'):  # ord为键盘输入对应的整数,
        cv2.imwrite('%s.jpg' % (str(num)), img)
        break

video.release()
# 如果不用release方法的话无法储存，要等结束程序再等摄像头关了才能显示保持成功
capture.release()  # 把摄像头也顺便关了

cv2.destroyAllWindows()
