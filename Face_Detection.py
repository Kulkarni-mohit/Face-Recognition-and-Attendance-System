import cv2 as cv
import numpy as np
from tensorflow import keras
import os
import matplotlib.pyplot as plt
import PIL
import Excel
import time

people=[]
for i in os.listdir(r'F:\PBL Project\Faces'):
    people.append(i)

models = keras.models.load_model('Model_1.h5')

def test(frame_test):
    #global models
    frame_test.resize((224,224,3),refcheck=False)
    y_pred = np.argmax(models.predict(np.expand_dims(np.array(frame_test), axis=0)), axis=-1)

    return y_pred


def Face_detection():
        

    model = "res10_300x300_ssd_iter_140000.caffemodel"
    configFile = 'deploy.prototxt.txt'
    net = cv.dnn.readNetFromCaffe(configFile,model)

    capture= cv.VideoCapture(0)
        
    while True:
        istrue, frame = capture.read()
            
        a = np.empty_like(frame)
        a[:] = frame
            
        h,w = frame.shape[:2]
        blob = cv.dnn.blobFromImage(cv.resize(frame,(300,300)),1.0,(300,300),(104.0,117.0,123.0))
        net.setInput(blob)
        faces = net.forward()

        for i in range(faces.shape[2]):
            confidence = faces[0,0,i,2]
            if confidence > 0.6:
                box = faces[0,0,i,3:7]*np.array([w,h,w,h])
                (x,y,x1,y1) = box.astype('int')

                name = test(frame)
                cv.rectangle(a,(x,y), (x1,y1),(0,0,255),2)    
                cv.putText(a,people[name[0]],(int(x),int(y)), cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
                Excel.excel(people[name[0]])
            
            cv.imshow('Detection Faces',a)
                        
        if cv.waitKey(20) & 0xFF==ord('q') :
            break
    capture.release()
    cv.destroyAllWindows()
    
    
Face_detection()
