# This script reads an image, resize its dimension and crops its size.

import cv2
import numpy as np

# Read the image
img = cv2.imread("Resources/gatin.png")

# Show image dimensions 
print(img.shape)

# Show image (post previous operations)
cv2.imshow("Original image", img)

# Change the dimensions
imgResized = cv2.resize(img, (600,350))

# Crop the image ( [:] stands for [0:350, 0:600], the whole image)
imgCropped = imgResized[:]

# Show image (post previous operations)
cv2.imshow("Image size adjusted", imgCropped)

print(imgCropped.shape)

# Time for image display, in milliseconds
cv2.waitKey(0)
