#rocketOC
#20170902
import cv2
import numpy as np

def barcode_interface():
	"""command line interface for creating barcodes"""
	vid_path = raw_input('path to video (e.g., videos/beachslop2.mov): ')
	if len(vid_path) == 0:
		vid_path = 'videos/beachslop2.mov'
	mod_frames = int(raw_input('read every x frames: '))
	pixels_per_frame = int(raw_input('pixel "stretch" per frame average (recommend 1): '))
	filename_output = raw_input('file name for output (e.g. output/barcode.png): ')
	btype = raw_input('barcode type of standard (s), horizontal (h), vertical (v), circle (c), or spiral (sp): ')
	if btype == 's': 
		bar_height = int(raw_input('barcode height dimension (in pixels): '))
		barcode(vid_path,mod_frames,bar_height,pixels_per_frame,filename_output)
	elif btype == 'h':
		barcode_horizontal(vid_path,mod_frames,pixels_per_frame,filename_output)
	elif btype == 'v':
		barcode_vertical(vid_path,mod_frames,pixels_per_frame,filename_output)
	elif btype == 'a':
		bar_height = int(raw_input('barcode height dimension (in pixels): '))
		barcode_all(vid_path,mod_frames,bar_height,pixels_per_frame,filename_output)
	elif btype == 'c':
		barcode_circle(vid_path,mod_frames,background=255,dim=1000,thickness=120
			,radius=400,filename_output=filename_output)
	elif btype == 'sp':
		barcode_spiral(vid_path,mod_frames,background=255,dim=1000,thickness=120
			,radius=300,filename_output=filename_output)
	else:
		print 'input not understood'


def barcode(vid_path,mod_frames,bar_height,pixels_per_frame,filename_output):
	"""create a barcode from an mp4 or mov"""
	vc = cv2.VideoCapture(vid_path)
	#get the number of frames. works with cv3
	num_frames = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
	bar_width = int(np.ceil(pixels_per_frame*np.floor(1+num_frames/mod_frames)))

	#print 'num frames:', num_frames, ' bar_width: ', bar_width, ' mod_frames: ', mod_frames
	blank = np.zeros((bar_height,bar_width,3)) #blank for barcode
	c=0
	blanki = 0

	if vc.isOpened():
		rval , frame = vc.read()
	else:
		rval = False

	while rval:
		if c % mod_frames == 0:
			# cv2.waitKey(1)
			try:
				blank[:,blanki:(blanki+pixels_per_frame)] = avg_pixel(frame)
			except IndexError:
				print 'Index Error: blanki: ', blanki, ';end: ', blanki+pixels_per_frame
			blanki = blanki + pixels_per_frame
			#print(str(np.round((c*100.0)/num_frames,1)) + '%') #progress
		rval, frame = vc.read()
		c = c + 1
	
	vc.release()
	cv2.imwrite(filename_output,blank)


def barcode_horizontal(vid_path,mod_frames,pixels_per_frame,filename_output):
	"""create a barcode from an mp4 or mov. y pixel in barcode corresponding that row's avg per frame"""
	vc = cv2.VideoCapture(vid_path)
	#get the number of frames. works with cv3
	num_frames = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
	bar_width = int(np.ceil(pixels_per_frame*np.floor(1+num_frames/mod_frames)))
	bar_height = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT)) # float

	blank = np.zeros((bar_height,bar_width,3)) #blank for barcode
	c=0
	blanki = 0

	if vc.isOpened():
		rval , frame = vc.read()
	else:
		rval = False

	while rval:
		if c % mod_frames == 0:
			# cv2.waitKey(1)
			try:
				for i in range(pixels_per_frame):
					blank[:,(blanki+i)] = avg_column(frame)
			except IndexError:
				print 'IndexError: blanki: ', blanki
			blanki = blanki + pixels_per_frame
			#print(str(np.round((c*100.0)/num_frames,1)) + '%') #progress
		rval, frame = vc.read()
		c = c + 1
	
	vc.release()
	cv2.imwrite(filename_output,blank)

def barcode_vertical(vid_path,mod_frames,pixels_per_frame,filename_output):
	"""create a barcode from an mp4 or mov. x pixel in barcode corresponding that column's avg per frame"""
	vc = cv2.VideoCapture(vid_path)
	#get the number of frames. works with cv3
	num_frames = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
	bar_width = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))
	bar_height = int(np.ceil(pixels_per_frame*np.floor(1+num_frames/mod_frames)))

	blank = np.zeros((bar_height,bar_width,3)) #blank for barcode
	c=0
	blanki = 0

	if vc.isOpened():
		rval , frame = vc.read()
	else:
		rval = False

	while rval:
		if c % mod_frames == 0:
			# cv2.waitKey(1)
			try:
				for i in range(pixels_per_frame):
					blank[(blanki+i),:] = avg_row(frame)
			except IndexError:
				print 'IndexError: blanki: ', blanki
			blanki = blanki + pixels_per_frame
			#print(str(np.round((c*100.0)/num_frames,1)) + '%') #progress
		rval, frame = vc.read()
		c = c + 1
	
	vc.release()
	cv2.imwrite(filename_output,blank)

def barcode_all(vid_path,mod_frames,bar_height,pixels_per_frame,filename_output):
	"""create all barcode types in a single run to avoid multiple video reads"""
	vc = cv2.VideoCapture(vid_path)
	#get the number of frames. works with cv3
	num_frames = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
	bar_width_v = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))
	bar_height_v = int(np.ceil(pixels_per_frame*np.floor(1+num_frames/mod_frames)))
	bar_width_h = int(np.ceil(pixels_per_frame*np.floor(1+num_frames/mod_frames)))
	bar_height_h = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))
	bar_width_s = int(np.ceil(pixels_per_frame*np.floor(1+num_frames/mod_frames)))
	bar_height_s = bar_height

	blank_v = np.zeros((bar_height_v,bar_width_v,3)) #blanks for barcode
	blank_h = np.zeros((bar_height_h,bar_width_h,3)) #blanks for barcode
	blank_s = np.zeros((bar_height_s,bar_width_s,3)) #blanks for barcode

	filenameparts = filename_output.split('.')
	filename_output_v = filenameparts[0] + '_v.' + filenameparts[1]
	filename_output_h = filenameparts[0] + '_h.' + filenameparts[1]
	filename_output_s = filenameparts[0] + '_s.' + filenameparts[1]

	c=0
	blanki = 0

	if vc.isOpened():
		rval , frame = vc.read()
	else:
		rval = False

	while rval:
		if c % mod_frames == 0:
			# cv2.waitKey(1)
			try:
				blank_s[:,blanki:(blanki+pixels_per_frame)] = avg_pixel(frame)
				for i in range(pixels_per_frame):
					blank_v[(blanki+i),:] = avg_row(frame)
					blank_h[:,(blanki+i)] = avg_column(frame)
			except IndexError:
				print 'IndexError: blanki', blanki
			blanki = blanki + pixels_per_frame
			print(str(np.round((c*100.0)/num_frames,1)) + '%') #progress
		rval, frame = vc.read()
		c = c + 1
	
	vc.release()
	cv2.imwrite(filename_output_v,blank_v)
	cv2.imwrite(filename_output_h,blank_h)
	cv2.imwrite(filename_output_s,blank_s)

def barcode_circle(vid_path,mod_frames,background,dim,thickness,radius,filename_output):
	"""create a circular barcode from an mp4 or mov.  If too many frames are used,
	the circle will collapse to a point because of the angle definition."""
	vc = cv2.VideoCapture(vid_path)
	num_frames = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
	bar_width = int(np.floor(1+num_frames/mod_frames))

	blank = np.zeros((bar_width,3)) #blank for barcode
	c=0
	blanki = 0

	if vc.isOpened():
		rval , frame = vc.read()
	else:
		rval = False

	while rval:
		if c % mod_frames == 0:
			# cv2.waitKey(1)
			try:
				blank[blanki] = avg_pixel(frame)
			except IndexError:
				print 'Index Error: blanki: ', blanki
			blanki = blanki + 1
			#print(str(np.round((c*100.0)/num_frames,1)) + '%') #progress
		rval, frame = vc.read()
		c = c + 1
	
	anglePerSnap = 360.0/blank.shape[0]
	blank_circle = np.ones((dim,dim,3))*background
	center = int(dim/2.0)
	for i, col in enumerate(blank):
		cv2.ellipse(blank_circle,(center,center),(radius,radius),-90+i*anglePerSnap,0,anglePerSnap,col,thickness)
	cv2.imwrite(filename_output,blank_circle)


def barcode_spiral(vid_path,mod_frames,background,dim,thickness,radius,filename_output):
	"""create a spiral barcode from an mp4 or mov.
	spiral is slight to avoid tail overlapping the head. If too many frames are used,
	the spiral will collapse to a point because of the angle definition."""
	vc = cv2.VideoCapture(vid_path)
	num_frames = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
	bar_width = int(np.floor(1+num_frames/mod_frames))

	blank = np.zeros((bar_width,3)) #blank for barcode
	c=0
	blanki = 0

	if vc.isOpened():
		rval , frame = vc.read()
	else:
		rval = False

	while rval:
		if c % mod_frames == 0:
			# cv2.waitKey(1)
			try:
				blank[blanki] = avg_pixel(frame)
			except IndexError:
				print 'Index Error: blanki: ', blanki
			blanki = blanki + 1
			#print(str(np.round((c*100.0)/num_frames,1)) + '%') #progress
		rval, frame = vc.read()
		c = c + 1
	
	anglePerSnap = 360.0/blank.shape[0]
	blank_circle = np.ones((dim,dim,3))*background
	center = int(dim/2.0)
	for i, col in enumerate(blank):
		rad = radius + int(thickness*(i*anglePerSnap)/360.0)
		cv2.ellipse(blank_circle,(center,center),(rad,rad),-90+i*anglePerSnap,0,anglePerSnap,col,thickness)
	#because the brush is circular, the tail is disproportionately represented, so cut it by the bg color
	#will look strange and disjointed if there are not sufficient frames
	cv2.ellipse(blank_circle,(center,center),(radius+thickness,radius+thickness),-90+anglePerSnap,0,1,(background,background,background),thickness)
	cv2.imwrite(filename_output,blank_circle)


def avg_pixel(frame):
	"""returns the average pixel value of a frame"""
	r = np.floor(np.mean(np.mean(frame,0),0))
	return r

def avg_column(frame):
	"""for this frame, return what the average column looks like.
	for an mxn image returns a 1xm array where m was number of rows"""
	r = np.floor(np.mean(frame,1))
	return r

def avg_row(frame):
	"""for this frame, return what the average row looks like.
	for an mxn image returns a 1xn array where n was number of columns"""
	r = np.floor(np.mean(frame,0))
	return r

if __name__ =="__main__":
	barcode_interface()

