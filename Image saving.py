import cv2 as cv
import os
import time


def captureimages(name, no_of_images=60):
    """
    name --> name of directory to be made
    """
    
    os.mkdir(name)
    os.chdir(name)
    
    capture = cv.VideoCapture(0)

    i = 0
    while True:
        istrue, frame = capture.read()

        time.sleep(1)
        filename = name+str(i)+'.jpg'
        cv.imwrite(filename, frame)
        i+=1
        if i == no_of_images:
            break

    capture.release()
    cv.destroyAllWindows()
    
    print('Image Saved Successfully')
    

def addimages(name,no_of_images):
    """
    name --> name of directory to be updated
    """

    os.chdir(name)

    capture = cv.VideoCapture(0)

    i = 0
    while True:
        istrue, frame = capture.read()

        time.sleep(1)
        filename = name+str(i)+'.jpg'
        cv.imwrite(filename, frame)
        i+=1
        if i == no_of_images:
            break

    capture.release()
    cv.destroyAllWindows()
    
    print('Image Saved Successfully')

captureimages('Mohit_Kulkarni',100)
