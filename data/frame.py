# Importing all necessary libraries
import cv2
import os
  
# Read the video from specified path
cam = cv2.VideoCapture("video.mp4")

# frame
currentframe = 0

try:
      
    # creating a folder named data
    if not os.path.exists('images'):
        os.makedirs('images')
  
# if not created then raise error
except OSError:
    print ('Error: Creating directory of images')

while(True):

    cam.set(cv2.CAP_PROP_POS_MSEC,(currentframe*1000))
      
    # reading from frame
    ret, frame = cam.read()
  
    if ret:
        # if video is still left continue creating images
        name = os.path.join("images", "frame") + str(currentframe) + '.png'
        print ('Creating...' + name)
  
        # writing the extracted images
        cv2.imwrite(name, frame)
  
        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break
  
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
