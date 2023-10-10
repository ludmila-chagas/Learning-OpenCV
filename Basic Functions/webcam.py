import cv2

# Defining frame dimensions
frameWidth = 640
frameHeight = 480

# Create a cap object instance from cv2.VideoCapture, to setup some properties of the video
cap = cv2.VideoCapture(0)

# Setting up the dimensions defined before (3 stands for width and 4 for height)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

# Setting up video brightness 
cap.set(10,150)

# Loop for continuously capturing and displaying the video
while True:
    
    # Capture each frame with cap
    success, img = cap.read()
    cv2.imshow("Result", img)

    # Define 'q' as exit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break