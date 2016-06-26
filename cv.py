#!/usr/bin/env python
# encoding: utf-8
import cv2

print(cv2.__version__)
drawing = False
top_left_pt, bottom_right_pt = (-1, -1), (-1, -1)
capture = cv2.VideoCapture(0)

if capture.isOpened() is False:
    raise IOError("Can't open webcam")
size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)


def draw_rectangle(event, x, y, flags, param):
    global x_init, y_init, drawing, top_left_pt, bottom_right_pt
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Mouse clicked @', (x, y))
        drawing = True
        x_init, y_init = x, y
        # cv2.putText(img,str(pre_position),cv2.)
    elif event == cv2.EVENT_LBUTTONUP:
        print('mouse released @', (x, y))
        drawing = False
        top_left_pt = (min(x, x_init), min(y, y_init))
        bottom_right_pt = (max(x, x_init), max(y, y_init))
        # img[y_init:y, x_init:x] = 255 - img[y_init:y, x_init:x]
        cv2.rectangle(img, top_left_pt, bottom_right_pt, (0, 255, 0), 1)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            top_left_pt = (min(x, x_init), min(y, y_init))
            bottom_right_pt = (max(x, x_init), max(y, y_init))
            # img[y_init:y, x_init:x] = 255 - img[y_init:y, x_init:x]
            cv2.rectangle(img, top_left_pt, bottom_right_pt, (0, 255, 0), 1)


cv2.namedWindow('Webcam')
cv2.setMouseCallback('Webcam', draw_rectangle)
num = 0
filename = ''
while True:
    ret, frame = capture.read()
    img = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
    (x0, y0), (x1, y1) = top_left_pt, bottom_right_pt
    # img[y0:y1, x0:x1] = 255 - img[y0:y1, x0:x1]
    cv2.rectangle(img, top_left_pt, bottom_right_pt, (0, 255, 0), 1)
    cv2.imshow('Webcam', img)
    key = cv2.waitKey(1)
    num = num + 1
    if key == 27:  # ord为键盘输入对应的整数,
        filename = str('%s.jpg' % (str(num)))
        print('Filename', filename)
        # cv2.imwrite(filename, img)

        break

capture.release()

cv2.destroyAllWindows()
