import os
import cv2
import numpy as np
from os import listdir
from sklearn import svm
from os.path import isfile, join

train_path = 'train/'
training_set = []
training_labels = []
images = [f for f in listdir(train_path) if isfile(join(train_path, f))]

i = 0
for file in images:
	if (os.path.getsize(train_path + str('/') + file)) != 0 :
		img = cv2.imread(train_path + file)
		res=cv2.resize(img,(250,250))
		gray_image = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
		xarr=np.squeeze(np.array(gray_image).astype(np.float32))
		m,v=cv2.PCACompute(xarr)
		arr= np.array(v)
		flat_arr= arr.ravel()
		training_set.append(flat_arr)
		i += 1
		if i < 49:
			training_labels.append(0)
		elif i > 48 and i < 96:
			training_labels.append(1)
		elif i > 95:
			training_labels.append(2)
		print i

trainData=np.float32(training_set)
responses=np.float32(training_labels)
print responses
#svm = cv2.SVM()
svm = svm.SVC()
svm.fit(trainData,responses)
#svm.save('svm_data.dat')

test_path = 'testing/'
testing_set = []
testing_labels = []
test = [f for f in listdir(test_path) if isfile(join(test_path, f))]

for file in test:
	if (os.path.getsize(test_path + str('/') + file)) != 0 :
		img = cv2.imread(test_path + file)
		res=cv2.resize(img,(250,250))
		gray_image = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
		xarr=np.squeeze(np.array(gray_image).astype(np.float32))
		m,v=cv2.PCACompute(xarr)
		arr= np.array(v)
		flat_arr= arr.ravel()
		testing_set.append(flat_arr)

testData=np.float32(testing_set)
responses=svm.predict(testData)
print responses
