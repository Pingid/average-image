import numpy as np
import os

from skimage import io
from skimage.transform import resize

def averageAll(imageList, filename):
	# export average
	avarage=np.median(imageList, axis=(0))
	io.imsave(filename, avarage)

def animate(imageList):
	# Loop through each image adding blend and saving
	blended=imageList[0]
	for idx, im in enumerate(imageList):
		blended=np.mean([blended, im], axis=(0))
		io.imsave('animation/' + 'pic' + str(idx).zfill(4) + '.png', blended)
		print(str(idx).zfill(4))

# Access all JPG files in directory
allfiles=os.listdir(os.getcwd() + '/images/')
imagefiles=[filename for filename in allfiles if  filename[-4:] in [".jpg",".jpeg"]]
imlist=[os.getcwd() + '/images/' + filename for filename in imagefiles]

# Resize images
resized=[resize(io.imread(im), (1080, 1080)) for im in imlist]

# animate(resized)
averageAll(resized, 'averageall.png')
