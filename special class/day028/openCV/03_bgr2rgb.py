# show image until 'esc' gets pressed

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("irene.jpg", cv.IMREAD_UNCHANGED)  # opencv에서는 BGR 순서로 색을 numpy에 저장
# matplotlib에서는 RGB순서로 색을 저장한다.

plt.imshow(img[:,:,::-1])   # convert from bgr to rgb
plt.xticks([]), plt.yticks([])
plt.show()
