import cv2

face=cv2.CascadeClassifier('Data/haarcascades/haarcascade_frontalface_default.xml')
smile=cv2.CascadeClassifier('Data/haarcascades/haarcascade_smile.xml')

y=0 

def detect_face(img):
    global y
    face_rects=face.detectMultiScale(img,scaleFactor=1.2,minNeighbors=5)
    for (fx,fy,fw,fh) in face_rects:
        x="Face detected-"+str(len(face_rects))
        cv2.putText(img,x,(0,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        pic=img[fy:fy+fh,fx:fx+fw]
        smile_rects=smile.detectMultiScale(pic,scaleFactor=1.8,minNeighbors=20)
        for (sx,sy,sw,sh) in smile_rects:
            cv2.putText(img,"You are smiling",(0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
            if(len(face_rects)*0.5 <=len(smile_rects)):
                y=y+1
                x="Photo\\"+str(y)+".jpg"
                cv2.imwrite(x,img)
    return img


cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    
    
    frame=detect_face(frame)
    cv2.imshow('video',frame)
    
    k=cv2.waitKey(1)
    if k==27:
        break
        
cap.release()
cv2.destroyAllWindows()