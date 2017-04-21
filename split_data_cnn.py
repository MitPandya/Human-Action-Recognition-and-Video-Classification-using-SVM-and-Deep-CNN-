import os.path
import cv2
import sys
import os
from shutil import rmtree
import math

global root_directory
root_directory = os.getcwd()

if len(sys.argv) != 2:
    print "Enter < train | test >"
    exit(1)

task = sys.argv[1]
if task not in ['train', 'test']:
	print "Enter < train | test >"
	exit(1)


def write_frames(file):
	vidcap = cv2.VideoCapture(read_dir+file.strip())
	frameRate = 10 #rame rate
	class_ = f.strip().split('/')[0]
	global classes
	c = classes[class_]
	path = write_dir+str(c)
	if not os.path.exists(path):
		os.makedirs(path)
		global count
		count = 0
	if os.getcwd() != path:
		os.chdir(path)
	while(vidcap.isOpened()):
		frameId = vidcap.get(1) #current frame number
		success, frame = vidcap.read()
		if (success != True):
			break
		if (frameId % math.floor(frameRate) == 0):
			cv2.imwrite("frame%d.png" % count, frame)
			count += 1
		if cv2.waitKey(10) == 27:
			break
	vidcap.release()
	os.chdir(root_directory)

read_dir = 'UCF101/'
if task == 'train':
	write_dir = 'classes/'
	file = open('train_list','r')
	if os.path.exists('classes'):
		rmtree('classes')
else:
	write_dir = 'test_set/'
	file = open('test_list','r')
	if os.path.exists('test_set'):
		rmtree('test_set')

global count
global classes
classes = {}
class_count = 0
count = 0
c = 0

for f in file:
	if os.path.exists(read_dir+f.strip()):
		class_ = f.strip().split('/')[0]
		if not class_ in classes:
			classes[class_] = class_count
			class_count += 1
		write_frames(f)
  		print "processed %d th video clip." %(c)
  		c += 1
file.close()
