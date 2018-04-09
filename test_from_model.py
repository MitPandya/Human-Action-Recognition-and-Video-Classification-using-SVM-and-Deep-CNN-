import os
import cv2
import numpy as np
from os import listdir
import sklearn
from sklearn import svm
from os.path import isfile, join
from sklearn.externals import joblib

# load svm from .pkl file
svm = joblib.load('svm.pkl')
print 'testing...'

path = 'test/'
testing_set = []
testing_labels = []

for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith((".png")):
        	print name
        	if (os.path.getsize(root + str('/') + name)) != 0 :
        		label = root.split('/')[1]
        		img = cv2.imread(root + str('/') + name)
        		#res=cv2.resize(img,(250,250))
        		res = img
        		gray_image = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        		xarr=np.squeeze(np.array(gray_image).astype(np.float32))
        		m,v=cv2.PCACompute(xarr, mean = np.array([]))
        		arr= np.array(v)
        		flat_arr= arr.ravel()
        		testing_set.append(flat_arr)
        		testing_labels.append(label)
t = 0
f = 0
testData = np.float32(testing_set)
responses = svm.predict(testData)

for i in range(len(responses)):
	if responses[i] == testing_labels[i]:
		t += 1
	else:
		f += 1

print responses
print set(responses)
print len(responses),' ', len(testing_labels)
print 'True ',t
print 'False ',f

file = open('results_svm.txt','w')
for i in range(len(responses)):
	file.write(testing_labels[i]+"  "+responses[i]+'\n')
file.close()
