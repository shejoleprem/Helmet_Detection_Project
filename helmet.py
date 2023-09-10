
import cv2
import torch
import pandas 
import numpy as np
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
path='F:/4th sem/4th_sem_projects/EDI_PROJECT/best.pt'
model=torch.hub.load('ultralytics/yolov5','custom',path,force_reload=True)
cap=cv2.VideoCapture("C:/Users/91957/Downloads/pexels-cottonbro-studio-5206886-3840x2160-25fps.mp4")
# videopath="C:/Users/91957/Downloads/pexels-cottonbro-studio-5206886-3840x2160-25fps.mp4"
while True:
    ret,frame=cap.read()
    frame = cv2.resize(frame, (600, 600))
    results=model(frame)
    frame=np.squeeze(results.render())
    cv2.imshow("Frame",frame)
    a=results.pandas().xyxy[0]
    
    for index,row in a.iterrows():
        confi=int(row['confidence']*100)
        print(confi)
        print(row['name'])
        if confi>50 and row['name']=='With Helmet':
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)
            
            print("connected")
        else:
           
            print("disconnect")
        
    if cv2.waitKey(1)&0xFF==27:
        
        print("disconnect")
        break
cap.release()
cv2.destroyAllWindows()
