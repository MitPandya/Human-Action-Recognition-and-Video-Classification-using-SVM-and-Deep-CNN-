import cv2
import sys
import os

if len(sys.argv) != 2:
    print "Enter <path_to_video>"
    exit(1)

video_path = sys.argv[1]
out_folder = video_path.split('.')[0]
output_dir = out_folder +str('_frames') + str("/")
main_dir = '/home/meet/video_classification'

def extract_image(file):
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
	print 'Error writing frames'