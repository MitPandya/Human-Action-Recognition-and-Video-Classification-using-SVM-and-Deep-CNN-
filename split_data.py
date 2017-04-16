import os.path
import cv2
import sys
import os

if len(sys.argv) != 2:
    print "Enter < train | test >"
    exit(1)

task = sys.argv[1]
if task not in ['train', 'test']:
	print "Enter < train | test >"
	exit(1)


def write_frames(file):
	vidcap = cv2.VideoCapture(read_dir+file.strip())
	success,image = vidcap.read()
	cur_class = file.strip().split('/')[0]
	path = write_dir+cur_class
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
	os.chdir('/home/meet/video_classification')

read_dir = 'UCF101/'
if task == 'train':
	write_dir = 'train/'
	file = open('train_list','r')
else:
	write_dir = 'test/'
	file = open('test_list','r')

global count
count = 0
c = 0
for f in file:
	c += 1
	if os.path.exists(read_dir+f.strip()):
		write_frames(f)
  		print "processed %d th video clip." %(c)
file.close()

'''def extract_image(file):
	vidcap = cv2.VideoCapture(file)
	success,image = vidcap.read()
	global count
	success = True
	os.chdir(main_dir+'/'+output_dir)
	print 'writing to ',output_dir
	while success:
  		success,image = vidcap.read()
  		cv2.imwrite("frame%d.png" % count, image)
  		if cv2.waitKey(10) == 27:
  			break
  		count += 1
try:
	data_list = os.listdir(video_path)
	os.mkdir(output_dir)
	k = 1
	global count
	count = 0
	for files in data_list:
		os.chdir(main_dir+'/'+video_path)
		extract_image(files)
		print "processed %d th video clip." %(k)
		k += 1
except:
	print 'Error writing frames' '''