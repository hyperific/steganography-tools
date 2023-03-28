def encode(imagesFolder, message, outDir):
   import numpy as np 
   from PIL import Image 
   import os
   import math 
   imagePaths = os.listdir(imagesFolder) 
   imgCount =0
   locA = (0,0)
   for i in np.arange(0,len(message),5):
   	if i+5>len(message):
   		chunk = message[i:len(message)]
   		d = i+5-len(message)
   		for a in range(d):
   			chunk=chunk + ' '
   	else:
   		chunk = message[i:i+5]
   	pixA = (imgCount,ord(chunk[0]),ord(chunk[1]))
   	pixB = (ord(chunk[2]),ord(chunk[3]),ord(chunk[4]))
   	img = Image.open(imagesFolder + '/'+imagePaths[imgCount])
   	w,h= img.size
   	locB = (w-1,h-1)
   	img.putpixel(locA,pixA)
   	img.putpixel(locB,pixB)
   	img.save(imagesFolder +'/' + outDir + '/' + str(imgCount)+'.png')
   	imgCount += 1
def decode(imagesFolder):
	import os
	from PIL import Image
	import numpy as np
	locA=(0,0)
	imagePaths = os.listdir(imagesFolder)
	imgIndices = []
	chunks =[]
	for i in range(len(imagePaths)):
		img = Image.open(imagesFolder+'/'+imagePaths[i])
		w,h = img.size
		locB = (w-1,h-1)
		pixA = img.getpixel(locA)
		pixB = img.getpixel(locB)
		imgIndices.append(pixA[0])
		chunk = chr(pixA[1])+chr(pixA[2])+chr(pixB[0])+chr(pixB[1])+chr(pixB[2])
		chunks.append(chunk)
	imgIndices=np.array(imgIndices)
	chunks=np.array(chunks)
	sort = np.argsort(imgIndices)
	message = "".join(chunks[sort])
		
	
	return message
	
	
	
	
	
