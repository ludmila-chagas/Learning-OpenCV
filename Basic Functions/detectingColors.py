import cv2
import numpy as np

# Empty function definition, to handle function createTrackBar parameters.
def empty(a):
    pass

# Images stacking function
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

# Creation of trackbar controls, starting with a new window definition followed by its resize. In adittion, we need to define 
# the minimum and maximum values of the trackbar, including a callback function that is required by createTrackBar function (empty).
path = 'Resources/gatinAdjusted.png'
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",37,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",116,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",251,255,empty)
cv2.createTrackbar("Val Min","TrackBars",50,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

# Start of the loop that make possible to apply in real time trackbar changes in HSV
while True:
    img = cv2.imread(path)

    # Converting color from RGB to HSV (Hue, Saturation, and Value/Brightness)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # Assigning HSV values based on trackbar positions
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    # Diplay of trackbar created
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    # Lower and upper scale definition
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    
    # Applying a mask to the original image, creating a new one, based on the active and inactive pixels of the mask
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    # cv2.imshow("Original",img)
    # cv2.imshow("HSV",imgHSV)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Result", imgResult)

    # Stacking the results together: original image, HSV, mask, and the new one
    imgStack = stackImages(0.6,([img,imgHSV],[mask,imgResult]))
    cv2.imshow("Stacked Images", imgStack)

    # Definition of image updates based on trackbar changes (1 millisecond practically enables real-time updates)
    cv2.waitKey(1)
