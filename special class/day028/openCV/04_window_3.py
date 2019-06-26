import cv2 as cv

img = cv.imread("irene.jpg", cv.IMREAD_UNCHANGED)  # opencv에서는 BGR 순서로 색을 numpy에 저장

# mac에서는 keyevent로 움직이는게 불가능한가???
# ten keyless도 고려하면 asdw로 ...
# asdw로 구현하자...

ESC = 27
arrowL = ord('a')
arrowR = ord('d')
arrowU = ord('w')
arrowD = ord('s')
delta = 10

row_num, col_num, _ = img.shape
x_pos = int(1680 / 2 - col_num / 2)
y_pos = int(1050 / 2 - row_num / 2)

cv.namedWindow('irene', cv.WINDOW_NORMAL)
cv.imshow('irene', img)
cv.resizeWindow('irene', col_num, row_num)
cv.moveWindow('irene', x_pos, y_pos)

while True:
    key = cv.waitKey()
    cv.moveWindow('irene', x_pos, y_pos)
    if key == arrowL:
        x_pos -= delta
    elif key == arrowR:
        x_pos += delta
    elif key == arrowU:
        y_pos -= delta
    elif key == arrowD:
        y_pos += delta
    elif key == ESC:
        break

cv.destroyAllWindows()