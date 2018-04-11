import os.path
import cv2
import sys
import os
from shutil import rmtree
import math
from datetime import datetime
import skvideo.io
import json

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
	metadata = skvideo.io.ffprobe(read_dir+file.strip())
	print(metadata.keys())
	frameRate = 10
	cur_class = file.strip().split('/')[0]
	path = write_dir+cur_class
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
	write_dir = 'train/'
	file = open('train_list','r')
	if os.path.exists('train'):
		rmtree('train')
else:
	write_dir = 'test/'
	file = open('test_list','r')
	if os.path.exists('test'):
		rmtree('test')
		
global count
count = 0
c = 0

for f in file:
	c += 1
	if os.path.exists(read_dir+f.strip()):
		write_frames(f)
  		print "processed %d th video clip." %(c)
file.close()
