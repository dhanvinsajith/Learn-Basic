import os
import cv2 as cv
import numpy as np

people = ['MarisaTomei', 'MingNaWen', 'OscarIsaac', 'PaulRudd']
DIR = r'C:\Users\dange\OneDrive\Desktop\learn\opencv\jasmcaus\face\photos\teach'

haar_cascade = cv.CascadeClassifier('face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
print('training')
create_train()
print('training done')
features = np.array(features, dtype = 'object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#training recognizer
face_recognizer.train(features, labels)

face_recognizer.save('face_trained_data.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)