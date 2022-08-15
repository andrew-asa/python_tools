import cv2 as cv
#检测函数
def face_detect_demo(img):
    gary=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    fp='/Users/andrew_asa/Documents/sofewareInstall/anaconda/anaconda3/envs/paddleenv/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml'
    face_detect=cv.CascadeClassifier(fp)
    face =face_detect.detectMultiScale(gary,minSize=(250,250),maxSize=(400,400))
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        cv.imshow('resuzt',img)


cap = cv.VideoCapture(0)
while True:
    flag,frame = cap.read()
    if not  flag:
        break
    face_detect_demo(frame)
    if ord('q') == cv.waitKey(0):
        break
cv.destroyAllWindows()
cap.release()
