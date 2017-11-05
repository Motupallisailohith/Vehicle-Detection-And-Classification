import cv2
import numpy as np

cars = 0
cap = cv2.VideoCapture('t.mp4')
bs = cv2.createBackgroundSubtractorMOG2()
car_c = cv2.CascadeClassifier('Car.xml')
while True:
    ret, frame = cap.read()
    if ret == True:
        #fgmask = bs.apply(frame)
        cv2.putText(frame,'Cars : ',(150, 250), cv2.FONT_HERSHEY_SIMPLEX, 2,(15,0,255),1,cv2.LINE_AA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('fgmask',fgmask)
        roi_c = frame[300:600,150:900]
        roi_b = gray[300:600,150:900]
        cv2.rectangle(frame,(150,300),(900,600),(255,0,0),2)
        car = car_c.detectMultiScale(roi_b, 1.3,5)
        for (x,y,w,h) in car:
            cv2.rectangle(roi_c, (x,y),(x+w,y+h),(0,0,255),3)
            cars+=1
            cv2.putText(frame,'Cars : '+str(cars),(150, 250), cv2.FONT_HERSHEY_SIMPLEX, 2,(15,0,255),1,cv2.LINE_AA)
        cv2.imshow('Frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
print "Total = "+cars

