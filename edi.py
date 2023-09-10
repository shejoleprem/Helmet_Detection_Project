import cv2
import torch
import pandas 
import numpy as np
from controller import servocontrol
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
path='F:/4th sem/4th_sem_projects/EDI_PROJECT/best1.pt'
model=torch.hub.load('ultralytics/yolov5','custom',path,force_reload=True)
cap=cv2.VideoCapture(1)

while True:
    ret,frame=cap.read()
    frame = cv2.resize(frame, (600, 600))
    results=model(frame)
    frame=np.squeeze(results.render())
    cv2.imshow("Frame",frame)
    a=results.pandas().xyxy[0]
    
    for index,row in a.iterrows():
        # print(row)
        x1=int(row['xmin'])
        y1=int(row['ymin'])
        x2=int(row['xmax'])
        y2=int(row['ymax'])
        
        confi=int(row['confidence']*100)
        print(confi)
        print(row['name'])
        if confi>60 and row['name']=='With Helmet':
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)
            servocontrol(1)
            print("connected")
        else:
            servocontrol(0)
            print("disconnect")
        
    if cv2.waitKey(1)&0xFF==27:
        servocontrol(0)
        print("disconnect")
        break
cap.realese()
cv2.destroyAllWindows()
