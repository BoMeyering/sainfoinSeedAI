## Sainfoin Seed Object Detection and Splitting ##
## Bo Meyering 2022                             ##

import os

# Dictionary of input and output directories for images
dir_list = dict(pods = './pods_output/', seeds = './seeds_output/', split = './split_output/')

def split_objects(src_path, output_dir, resize=False, output_dim=None):
	"""
	Takes an image file stored as a numpy array
	Identifies objects using Canny Edge detection and contour finding
	Saves each individual file in the desired output location
	"""
	import cv2
	import string
	import random

	src = cv2.imread(src_path)
	edges = cv2.Canny(src, 100, 200) # detect edges
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) # create kernel for edge closing operations
	closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel) 
	conts, __ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #find object external contours
	for c in conts:
		x, y, w, h = cv2.boundingRect(c)
		# M = cv2.moments(c)
		if w > 30 and h >30:
			maxdim = max(h, w)
			BUFFER = round(maxdim*.05) # set buffer around edges at 5% of maximum dimension
			cropped = src[y-BUFFER:y+maxdim+BUFFER, x-BUFFER:x+maxdim+BUFFER]
			filename = output_dir + ''.join(random.choices(string.hexdigits, k=15)) + '.JPG' # filenames are random hexadecimal strings
			if resize ==True and output_dim is not None:
				resized = cv2.resize(cropped, output_dim)
				cv2.imwrite(filename, resized)
			else:
				cv2.imwrite(filename, cropped)

for d in dir_list.keys():
	if os.path.exists(dir_list[d]) == False: # create output directories if none exist
		os.mkdir(dir_list[d])
	for root, dirs, files in os.walk(os.path.relpath(str(d))):
		img_list = [os.path.join(root, file) for file in files]
	for img in img_list:
		split_objects(img, dir_list[d], resize = True, output_dim = (150, 150))

