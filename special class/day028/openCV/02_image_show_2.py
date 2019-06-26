# show image until 'esc' gets pressed

import cv2 as cv

img = cv.imread("irene.jpg", cv.IMREAD_UNCHANGED)  # opencv에서는 BGR 순서로 색을 numpy에 저장

ESC = 27

cv.imshow('img', img)   #윈도우 창이 생성되면서
while True:
    key = cv.waitKey()
    print(key)
    if key == ESC:
        break

# 이거 없으면 바로 실행이 종료된다. 입력값을 받을 때 까지 대기한다.
# ms단위로 시간을 지정할 수 있다. && 입력값을 반환한다.

