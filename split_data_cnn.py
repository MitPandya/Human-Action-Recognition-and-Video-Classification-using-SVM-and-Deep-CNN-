import os.path
import cv2
import sys
import os
from shutil import rmtree

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
	class_ = f.strip().split('/')[0]
	global classes
	c = classes[class_]
	success,image = vidcap.read()
	path = write_dir+str(c)
	if not os.path.exists(path):
		os.makedirs(path)
		global count
		count = 0
	if os.getcwd() != path:
		os.chdir(path)
	while success:
		success,image = vidcap.read()
		cv2.imwrite("frame%d.png" % count, image)
		if cv2.waitKey(10) == 27:
			break
		count += 1
	os.chdir(root_directory)

read_dir = 'UCF101/'
if task == 'train':
	write_dir = 'classes/'
	file = open('train_list','r')
else:
	write_dir = 'test_set/'
	file = open('test_list','r')

global count
global classes
classes = {}
class_count = 0
count = 0
c = 0
if os.path.exists('classes'):
	rmtree('classes')
if os.path.exists('test_set'):
	rmtree('test_set')

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
