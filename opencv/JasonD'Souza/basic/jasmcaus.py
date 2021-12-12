import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


#READING IMAGES
'''
img = cv.imread('photos/ball.jpg')
cv.imshow('Ball', img)

cv.waitKey(0)
'''


#READING VIDEOS
'''
capture = cv.VideoCapture('videos/butterfly.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Butterfly', frame)

    if cv.waitKey(20) and 0xFF == ord('x'):
        break

capture.release()
cv.destroyAllWindows()
'''


#RESIZING (run live video without image or video)
'''
capture = cv.VideoCapture('videos/butterfly.mp4')
img = cv.imread('photos/ball.jpg')

#rescale function(images, video, live video)
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

#for image
resized_image = rescaleFrame(img, 0.25)
cv.imshow('Ball', resized_image)

#for video
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 3)
    cv.imshow('Butterfly', frame_resized)
    if cv.waitKey(20) and 0xFF == ord('d'):
        break
''''''
#for live video
capture_live = cv.VideoCapture(0)

def changeRes(width, height):
    capture_live.set(3, width)
    capture_live.set(4, height)

changeRes(200, 200)
while True:
    isitTrue, liveframe = capture_live.read()
    cv.imshow('Webcam', liveframe)
    c = cv.waitKey(1)
    if c == 27:
        break
''''''
capture.release()
capture_live.release()
cv.destroyAllWindows()
'''


#DRAWING SHAPES AND ADDING TEXT
'''
blank = np.zeros((500, 500, 3), dtype = 'uint8')
img = cv.imread('photos/ball.jpg')
'''
'''
#whole window turquoise
blank[:] = 207, 224, 64
cv.imshow('Turquoise', blank)
'''
'''
#small fill square turquoise
blank[200:300, 200:300] = 207, 224, 64
cv.imshow('Turquoise Square', blank)
'''
'''
#rectangle turquoise
cv.rectangle(blank, (175,125), (325,375), (207, 224, 64), thickness = 2)
cv.rectangle(blank, (25,225), (100,275), (207, 224, 64), thickness = 5)
cv.rectangle(blank, (350,225), (400,275), (207, 224, 64), thickness = cv.FILLED) #or thickness = -1
cv.imshow('Turquoise Rectangles', blank)
'''
'''
#circle turquoise
cv.circle(blank, (250, 250), 50, (207, 224, 64), thickness = 3)
cv.circle(blank, (250, 250), 75, (207, 224, 64), thickness = 3)
cv.circle(blank, (100, 100), 60, (207, 224, 64), thickness = -1)
cv.circle(blank, (350, 350), 125, (207, 224, 64), thickness = 10)
cv.circle(blank, (250, 250), 225, (207, 224, 64), thickness = 1)
cv.imshow('Turquoise Circles', blank)
'''
'''
#line turquoise
cv.line(blank, (150, 250), (350, 250), (207, 224, 64), thickness = 2)
cv.line(blank, (100, 200), (400, 300), (207, 224, 64), thickness = 2)
cv.line(blank, (200, 300), (300, 200), (207, 224, 64), thickness = 10)
cv.line(blank, (250, 50), (250, 450), (207, 224, 64), thickness = 1)
cv.line(blank, (25, 25), (475, 475), (207, 224, 64), thickness = 2)
cv.line(blank, (50, 25), (175, 475), (207, 224, 64), thickness = 5)
cv.imshow('Turquoise Lines', blank)
'''
'''
#text on image
cv.putText(blank, 'Hello World!', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (207, 224, 64), thickness = 2)
cv.putText(blank, 'second TEXT', (100, 100), cv.FONT_HERSHEY_COMPLEX, 1.5, (207, 224, 64), thickness = 2)
cv.putText(blank, 'ThIrD', (100, 350), cv.FONT_HERSHEY_DUPLEX, 4, (207, 224, 64), thickness = 1)
cv.putText(blank, 'fourth(?), text.!', (50, 175), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (207, 224, 64), thickness = 5)
cv.putText(blank, 'fifth', (100, 400), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (207, 224, 64), thickness = 1)
cv.putText(blank, 'sixth', (100, 450), cv.FONT_ITALIC, 0.75, (207, 224, 64), thickness = 1)
cv.putText(blank, 'seventh', (175, 450), cv.FONT_HERSHEY_PLAIN, 5, (207, 224, 64), thickness = 2)
cv.imshow('Turquoise Text', blank)
'''
'''
cv.waitKey(0)
'''


#ESSENTIAL FUNCTIONS
'''
img = cv.imread('photos/ball.jpg')
cv.imshow('Ball', img)
'''
'''
#image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Ball', gray)
'''
'''
#blur image
blur = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT) #change (9, 9) to change blur strength
cv.imshow('Blur Ball', blur)
'''
'''
#edge cascading
canny = cv.Canny(img, 75, 130) #blur and pass in blurred image to reduce number of edges
cv.imshow('Ball Edges', canny)
'''
'''
#dilate edges
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 100, 150)
dilated = cv.dilate(canny, (9, 9), iterations = 2)
cv.imshow('Dilated Ball Edges', dilated)
'''
'''
#eroding dilated image
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 100, 150)
dilated = cv.dilate(canny, (9, 9), iterations = 1)
eroded = cv.erode(dilated, (3, 3), iterations = 1)
cv.imshow('Eroded Ball', eroded)
'''
'''
#resizing image
resized1 = cv.resize(img, (750, 250), interpolation = cv,cv.INTER_CUBIC)
resized2 = cv.resize(img, (75, 75), interpolation = cv.INTER_AREA) #do inter_area part if shrinking
cv.imshow('Resized Ball 1', resized1)
cv.imshow('Resized Ball 2', resized2)
'''
'''
#cropping image
cropped = img[50:200, 200:400]
cv.imshow('Cropped Ball', cropped)
'''
'''
cv.waitKey(0)
'''


#IMAGE TRANSFORMATIONS
'''
img = cv.imread('photos/ball.jpg')
cv.imshow('Ball', img)
'''
'''
#translation(position)
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 75, 110) # negative x will move it left and negative y will move it up
cv.imshow('Translate', translated)
'''
'''
#rotation
def rotate(image, angle, rotPoint = None):
    (height, width) = image.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimemsions = (width, height)

    return cv.warpAffine(image, rotMat, dimemsions)

rotated = rotate(img, 135) # negative will rotate it clockwise
cv.imshow('Rotate', rotated)
#you can also rotate an already rotated image, BUT the previously rotated image will include the blank spaces too
'''
'''
#resizing
resized = cv.resize(img, (200, 200), interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resized)
'''
'''
#flipping
flip = cv.flip(img, 1) #0 means flipping image vertically, 1 means flipping horizontally, -1 means both vertical and horizontally
cv.imshow('Flipped', flip)
'''
'''
#cropping
cropped = img[100:300, 150:350] #(y, x)
cv.imshow('Cropped', cropped)
'''
'''
cv.waitKey(0)
'''


#CONTOUR DETECTION - boundaries/edges (either method 1 or 2 not both)
'''
img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)
blank = np.zeros(img.shape, dtype = np.uint8)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
'''
'''
#method 1 for edge detection
blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)
contours, heirarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
'''
'''
#method 2 for edge detection
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)
contours, heirarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
'''
'''
print(f'{len(contours)} contours found in cats.jpg')

cv.drawContours(blank, contours, -1, (0, 255, 0), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
'''


#COLOR SPACES
'''
img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)
'''
'''
#BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
#back
bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('Gray to BGR', bgr)
'''
'''
#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)
#back
bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', bgr)
'''
'''
#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)
#back
bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB to BGR', bgr)
'''
'''
#BGR to RGB (for using outside of opencv)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
'''
'''
cv.waitKey(0)
'''


#COLOR CHANNELS
'''
img = cv.imread('photos/cats.jpg')
blank = np.zeros(img.shape[:2], dtype = np.uint8)
cv.imshow('Cats', img)

b, g, r = cv.split(img) #seperating the color channels
cv.imshow('Blue', b)
cv.imshow('Red', r)
cv.imshow('Green', g)

print(img.shape) #3 on the main image shows the three color channels
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r]) #merge three seperate color channels
cv.imshow('Merged', merged)

blue = cv.merge([b, blank, blank]) #showing seperate color channels in their own colors
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

cv.waitKey(0)
'''


#DIFFERENT BLURRING TECHNIQUES
'''
img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)
'''
'''
#averaging (mean intensities)
avg = cv.blur(img, (5, 5))
cv.imshow('Averaging', avg)
'''
'''
#gaussian blur (mean weights)
gaus = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow('Gaussian Blur', gaus)
'''
'''
#median blur (median intensities)
med = cv.medianBlur(img, 5)
cv.imshow('Median Blur', med)
'''
'''
#bilateral (blurs but retains edges)
bil = cv.bilateralFilter(img, 10, 40, 30) #(source image, diameter, number of colors in surroundings considered, area around pixel considered)
cv.imshow('Bliateral Blurring', bil)
'''
'''
cv.waitKey(0)
'''


#BITWISE OPERATIONS
'''
blank = np.zeros((400, 400), dtype = 'uint8')
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

#'and' operation (common areas of both)
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('AND', bitwise_and)

#'or' operation (total area of both)
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('OR', bitwise_or)

#'xor' operation (total area - intersecting area)
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('XOR', bitwise_xor)

#'not' operation (everything outside area)
bitwise_notr = cv.bitwise_not(rectangle)
bitwise_notc = cv.bitwise_not(circle)
cv.imshow('NOT rectangle', bitwise_notr)
cv.imshow('NOT circle', bitwise_notc)

cv.waitKey(0)
'''


#MASKING
'''
img = cv.imread('photos/cats.jpg')
blank = np.zeros(img.shape[:2], dtype = np.uint8)
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2 - 50), 100, 255, -1) #mask has to be same size
masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow('Cats', img)
cv.imshow('Masked', masked)

cv.waitKey(0)
'''


#HISTOGRAM COMPUTATION
'''
img = cv.imread('photos/morecats.jpg')
blank = np.zeros(img.shape[:2], dtype = np.uint8)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2 - 50), 200, 255, -1)
cv.imshow('Gray', gray)
cv.imshow('Cats', img)
'''
'''
#grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()
'''
'''
#masked grayscale histogram
mask_hist = cv.calcHist([gray], [0], circle, [256], [0, 256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
plt.plot(mask_hist)
plt.xlim([0, 256])
plt.show()
'''
'''
#color histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])
plt.show()
'''
'''
cv.waitKey(0)
'''


#THRESHOLDING
'''
img = cv.imread('photos/morecats.jpg')
cv.imshow('Cats', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
'''
'''
#simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholding', thresh)
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse Simple Thresholding', thresh_inv)
'''
'''
#adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 13, 3)
adaptive_thresh_gauss = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 17, 3)
cv.imshow('Adaptive Thresholding Mean', adaptive_thresh)
cv.imshow('Adaptive Thresholding Gaussian', adaptive_thresh_gauss)
'''
'''
cv.waitKey(0)
'''


#EDGE DETECTION
'''
img = cv.imread('photos/cats.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Cats', img)
'''
'''
#laplacian method
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)
'''
'''
#soble method
sobx = cv.Sobel(gray, cv.CV_64F, 1, 0)
soby = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined = cv.bitwise_or(sobx, soby)
cv.imshow('SobelX', sobx)
cv.imshow('SobelY', soby)
cv.imshow('Combined Sobel', combined)
'''
'''
#canny method
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)
'''
'''
cv.waitKey(0)
'''