import os
import cv2
import numpy as np
from os import listdir
from sklearn import svm
from os.path import isfile, join
from sklearn.externals import joblib

path = 'train/'
training_set = []
training_labels = []

print 'training...'
for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith((".png")):
        	if (os.path.getsize(root + str('/') + name)) != 0 :
        		label = root.split('/')[1]
        		img = cv2.imread(root +str('/')+ name)
        		res = cv2.resize(img,(250,250))
        		gray_image = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        		xarr = np.squeeze(np.array(gray_image).astype(np.float32))
        		m,v = cv2.PCACompute(xarr)
        		arr = np.array(v)
        		flat_arr = arr.ravel()
        		training_set.append(flat_arr)
        		training_labels.append(label)

trainData = np.float32(training_set)
responses = training_labels
#svm = cv2.SVM()
svm = svm.SVC()
svm.fit(trainData,responses)
joblib.dump(svm, 'svm.pkl')
#svm.save('svm_data.dat')
print 'training done!'
print 'testing...'

path = 'test/'
testing_set = []
testing_labels = []

for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith((".png")):
        	if (os.path.getsize(root + str('/') + name)) != 0 :
        		img = cv2.imread(root + str('/') + name)
        		res=cv2.resize(img,(250,250))
        		gray_image = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        		xarr=np.squeeze(np.array(gray_image).astype(np.float32))
        		m,v=cv2.PCACompute(xarr)
        		arr= np.array(v)
        		flat_arr= arr.ravel()
        		testing_set.append(flat_arr)

testData = np.float32(testing_set)
responses = svm.predict(testData)

print responses
print set(responses)