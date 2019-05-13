import numpy as np
import cv2

dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX

face_1 = np.load('ravi.npy').reshape(100,50*50*3)
face_2 = np.load('ravi.npy').reshape(100,50*50*3)

users = {0:'Ravi_1',1:'Ravi_2'}

labels = np.zeros((200,1))
labels[:100,:] = 0.0
labels[100:,:] = 1.0

data = np.concatenate([face_1,face_2])

def dist(x1,x2):
    return np.sqrt(sum((x2 - x1)**2))

def knn(x,train,k=5):
    n = train.shape[0]
    distance = []
    for i in range(n):
        distance.append(dist(x,train[i]))
    distance = np.asarray(distance)
    sortedIndex = np.argsort(distance)
    lab = labels[sortedIndex][:k]
    count = np.unique(lab,return_counts = True)
    return count[0][np.argmax(count[1])]

while True:
    ret, img = capture.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray,1.3)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),5)
            myFace = img[y:y+h, x:x+w, :]
            myFace = cv2.resize(myFace, (50,50))
            label = knn(myFace.flatten(), data)
            userName = users[int(label)]
            
            cv2.putText(img,userName,(x,y), font,1, (0,255,0),2)
            
        cv2.imshow('result',img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        print("Camera Not Working")

capture.release()
cv2.destroyAllWindows()














