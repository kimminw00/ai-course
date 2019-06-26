import cv2 as cv

# 톱니바퀴에서 unpinned mode

#img = cv.imread("irene.jpg", cv.IMREAD_UNCHANGED)  # 원본 그대로 읽겠다는 의미, 3차원으로 읽어짐

img = cv.imread("irene.jpg", cv.IMREAD_GRAYSCALE)  # 2차원으로 읽어짐 == 색값이 하나니까

print(img)

print(img.shape, img.dtype)
# shape : 세로(행의 수), 가로(열의 수), 색(3가지)

# ctrl + f5 누르면 이전에 실행했던 거 다시 실행

