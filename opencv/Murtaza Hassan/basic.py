import cv2 as cv
import numpy as np

#CHAPTER 1 - READING
'''
#image
img = cv.imread('photos/ball.jpg')
cv.imshow('Ball', img)
cv.waitKey(0)
'''
'''
#videos
vid = cv.VideoCapture('videos/butterfly.mp4')
while True:
    isTrue, frame = vid.read()
    cv.imshow('Butterfly', frame)
    c = cv.waitKey(1)
    if c == 27:
        break
vid.release()
cv.destroyAllWindows()
'''
'''
#live feed
vid = cv.VideoCapture(0)
vid.set(3, 1080)
vid.set(4, 720)
vid.set(10, 150)
while True:
    isTrue, frame = vid.read()
    cv.imshow('Butterfly', frame)
    c = cv.waitKey(1)
    if c == 27:
        break
vid.release()
cv.destroyAllWindows()
'''


#CHAPTER 2 - BASIC FUNCTIONS
'''
img = cv.imread('photos/ball.jpg')
cv.imshow('Ball', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Ball', gray)
blur = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow('Blurred Ball', blur)
canny = cv.Canny(img, 100, 250)
cv.imshow('Canny Edged Ball', canny)
dilate = cv.dilate(canny, np.ones((5, 5), np.uint8), iterations = 1)
cv.imshow('Dilated', dilate)
erode = cv.erode(dilate, np.ones((5, 5), np.uint8), iterations = 1)
cv.imshow('Eroded', erode)

cv.waitKey(0)
'''


#CHAPTER 3 - RESIZING AND CROPPING
'''
img = cv.imread('photos/ball.jpg')
cv.imshow('Ball', img)
resize1 = cv.resize(img, (1080, 720))
resize2 = cv.resize(img, (120, 120))
cv.imshow('Big', resize1)
cv.imshow('Smol', resize2)
cropped = img[100:250, 100:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
'''


#CHAPTER 4 - SHAPES AND TEXT
'''
img = np.zeros((500, 500, 3), dtype = 'uint8')
cv.rectangle(img, (0, 0), (500, 500), (0, 255, 0), thickness = 5)
cv.rectangle(img, (200, 200), (300, 300), (0, 255, 0), thickness = -1)
cv.line(img, (200, 100), (300, 100), (0, 255, 0), thickness = 2)
cv.line(img, (200, 400), (300, 400), (0, 255, 0), thickness = 2)
cv.line(img, (100, 200), (100, 300), (0, 255, 0), thickness = 2)
cv.line(img, (400, 200), (400, 300), (0, 255, 0), thickness = 2)
cv.line(img, (300, 100), (400, 200), (0, 255, 0), thickness = 2)
cv.line(img, (400, 300), (300, 400), (0, 255, 0), thickness = 2)
cv.line(img, (200, 400), (100, 300), (0, 255, 0), thickness = 2)
cv.line(img, (100, 200), (200, 100), (0, 255, 0), thickness = 2)
cv.line(img, (50, 110), (50, 50), (0, 255, 0), thickness = 2)
cv.line(img, (110, 50), (50, 50), (0, 255, 0), thickness = 2)
cv.line(img, (450, 390), (450, 450), (0, 255, 0), thickness = 2)
cv.line(img, (390, 450), (450, 450), (0, 255, 0), thickness = 2)
cv.line(img, (50, 390), (50, 450), (0, 255, 0), thickness = 2)
cv.line(img, (110, 450), (50, 450), (0, 255, 0), thickness = 2)
cv.line(img, (450, 110), (450, 50), (0, 255, 0), thickness = 2)
cv.line(img, (390, 50), (450, 50), (0, 255, 0), thickness = 2)
cv.line(img, (300, 100), (100, 300), (0, 255, 0), thickness = 2)
cv.line(img, (200, 100), (400, 300), (0, 255, 0), thickness = 2)
cv.line(img, (200, 400), (400, 200), (0, 255, 0), thickness = 2)
cv.line(img, (300, 400), (100, 200), (0, 255, 0), thickness = 2)
cv.line(img, (400, 200), (100, 200), (0, 255, 0), thickness = 2)
cv.line(img, (400, 300), (100, 300), (0, 255, 0), thickness = 2)
cv.line(img, (200, 100), (200, 400), (0, 255, 0), thickness = 2)
cv.line(img, (300, 100), (300, 400), (0, 255, 0), thickness = 2)
cv.circle(img, (250, 250), 158, (0, 255, 0), thickness = 2)
cv.imshow('Design', img)

text = np.zeros((500, 500, 3), dtype = 'uint8')
cv.putText(text,'Hello World!', (100, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), thickness = 2)
cv.putText(text,'Hello World_Complex!', (50, 300), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), thickness = 2)
cv.imshow('Text', text)

cv.waitKey(0)
'''


#CHAPTER 5 - WARP PERSPECTIVE
'''
img = cv.imread('photos/cards.jpg')
cv.imshow('Cards', img)

width, height = 250, 350
pts = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]]) 
matrix = cv.getPerspectiveTransform(pts, pts2)
output = cv.warpPerspective(img, matrix, (width, height))
cv.imshow('Warped', output)

cv.waitKey(0)
'''


#CHAPTER 6 - JOINING IMAGES
'''
img = cv.imread('photos/ball.jpg')
img2 = cv.imread('photos/cards.jpg')
cv.imshow('Cards', img)

#method 1 - wont work if number of channels are different
imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))
cv.imshow('Horizontal Stack', imgHor)
cv.imshow('Vertical Stack', imgVer)

cv.waitKey(0)
'''


#CHAPTER 7 - COLOR DETECTION
'''
def empty(a):
    pass

cv.namedWindow('Track Bars')
cv.resizeWindow('Track Bars', 640, 240)
cv.createTrackbar('Hue Min', 'Track Bars', 0, 179, empty)
cv.createTrackbar('Hue Max', 'Track Bars', 179, 179, empty)
cv.createTrackbar('Sat Min', 'Track Bars', 130, 255, empty)
cv.createTrackbar('Sat Max', 'Track Bars', 208, 255, empty)
cv.createTrackbar('Val Min', 'Track Bars', 0, 255, empty)
cv.createTrackbar('Val Max', 'Track Bars', 255, 255, empty)

while True:
    img = cv.imread('photos/ball.jpg')

    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos('Hue Min', 'Track Bars')
    h_max = cv.getTrackbarPos('Hue Max', 'Track Bars')
    s_min = cv.getTrackbarPos('Sat Min', 'Track Bars')
    s_max = cv.getTrackbarPos('Sat Max', 'Track Bars')
    v_min = cv.getTrackbarPos('Val Min', 'Track Bars')
    v_max = cv.getTrackbarPos('Val Max', 'Track Bars')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(img_hsv, lower, upper)

    result = cv.bitwise_and(img, img, mask = mask)

    cv.imshow('Ball', img)
    cv.imshow('Mask', mask)
    cv.imshow('Result', result)


    cv.waitKey(1)
'''


#CHAPTER 8 - SHAPES
'''
def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) #RETR_EXTERNAL retreives outer contours
    for cnt in contours:
        area  = cv.contourArea(cnt)
        print(area)
        if area > 500:
            cv.drawContours(img_cnt, cnt, -1, (0, 255, 0), 3)
            perimeter = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02*perimeter, True)
            print(len(approx))

            obj_corners = len(approx)
            x, y, w, h = cv.boundingRect(approx)

            object_type = "None"
            if obj_corners == 3:
                object_type = "Tri"
            elif obj_corners == 4:
                if w/float(h) > 0.95 and w/float(h) < 1.05:
                    object_type = "Square"
                else:
                    object_type = "Rect"
            elif obj_corners > 4:
                object_type = "Circle"

            cv.rectangle(img_cnt, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv.putText(img_cnt, object_type, (x+(w//2)-10, y+(h//2)-10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

img = cv.imread('photos/shapes.png')
img_cnt = img.copy()
cv.imshow('Raw Shapes', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (7, 7), 1)
canny = cv.Canny(blur, 125, 175)
getContours(canny)

cv.imshow('Edge Shapes', canny)
cv.imshow('Drawn Shapes', img_cnt)


cv.waitKey(0)
'''


#CHAPTER 9 - FACE DETECTION
'''
capture = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier('face.xml')
while capture.isOpened():
    isItTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness = 2)
    cv.imshow('Webcam', frame)
    c = cv.waitKey(1)
    if c == 27:
        break

capture.release()
cv.destroyAllWindows()
'''