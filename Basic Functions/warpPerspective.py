import cv2
import numpy as np

img = cv2.imread("Resources/placa.webp")
cv2.imwrite("Resources/placa.png", img)

width,height = 350,250
pts1 = np.float32([[212,73],[522,7],[208,281],[497,327]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)


# 272,73- left top
# 522,7- right top
# 208,281-left bottom
# 497,327- right bottom