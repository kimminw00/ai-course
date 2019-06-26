import cv2 as cv

img = cv.imread('irene.jpg', cv.IMREAD_UNCHANGED)

cv.namedWindow('irene', cv.WINDOW_NORMAL)  # resize 가능
row_num, col_num, _ = img.shape

cv.imshow('irene', img)
cv.moveWindow('irene', int(1680 / 2 - col_num / 2), int(1050 / 2 - row_num / 2))  # 해상도로 중심을 알 수 있다.
cv.resizeWindow('irene', col_num, row_num)

for i in range(1, 8):
    cv.moveWindow('irene', int(1680 / 2 - col_num / 2), int(1050 / 2 - row_num / 2))  # 해상도로 중심을 알 수 있다.
    cv.resizeWindow('irene', col_num, row_num)
    cv.waitKey(2000)
    row_num = int(row_num * 1.1)
    col_num = int(col_num * 1.1)

cv.destroyAllWindows()