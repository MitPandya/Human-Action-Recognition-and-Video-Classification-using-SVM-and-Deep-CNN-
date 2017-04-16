import cv2
import matplotlib.pyplot as plt

input_folder = 'v_ApplyEyeMakeup_g01_c01/'
img = cv2.imread(input_folder + 'frame0.jpg')

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
#plt.savefig("plot.png")