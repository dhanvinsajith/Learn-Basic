import cv2 as cv

#FOR IMAGES
'''
img = cv.imread('photos/keanu_reeves.jpg')
cv.imshow('Keanu Reeves', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3) #increase minNeighbors to decrease sensitivity

print(f'number of faces: {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness = 2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)
'''


#FOR LIVE VIDEO
'''
capture_live = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier('face.xml')
while capture_live.isOpened():
    isitTrue, liveframe = capture_live.read()
    gray = cv.cvtColor(liveframe, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)
    for (x, y, w, h) in faces_rect:
        cv.rectangle(liveframe, (x, y), (x+w, y+h), (0, 0, 255), thickness = 2)
    cv.imshow('Webcam', liveframe)
    c = cv.waitKey(1)
    if c == 27:
        break

capture_live.release()
cv.destroyAllWindows()
cv.waitKey(0)
'''