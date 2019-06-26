import cv2 as cv

img = cv.imread('irene.jpg', cv.IMREAD_UNCHANGED)

cv.namedWindow('img')  # window를 생성시킴
cv.moveWindow('img', 0, 0)  # 표시되는 창의 위치를 옮김
cv.imshow('img', img)  # 'img'라는 윈도우가 없으면 새로 만든다. 있으면 윈도우에 img를 표시
cv.waitKey()
cv.moveWindow('img', 400, 400)  # 버튼을 한 번 누르면 창을 이동시킴
cv.waitKey()
cv.destroyAllWindows()


# normal과 autosize의 차이
cv.namedWindow('img-autosize', cv.WINDOW_AUTOSIZE)  # resize 불가능
cv.namedWindow('img-normal', cv.WINDOW_NORMAL)  # resize 가능
cv.resizeWindow('img-autosize', 700, 700)  # 한 번 창이 생성되면 창의 크기조절이 불가능하다.
cv.resizeWindow('img-normal', 700, 700)
cv.imshow('img-autosize', img)
cv.imshow('img-normal', img)
cv.waitKey()
cv.destroyAllWindows()

