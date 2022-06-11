# import cv2 library
import cv2
import numpy as np

def concat_vh(list_2d):
    
      # return final image
    return cv2.vconcat([cv2.hconcat(list_h) 
                        for list_h in list_2d])
                        
# read the images
img = []
row =[]
for i in range(1,576):
	print("open ./input/"+str(i)+'.png')
	row.append(cv2.imread("./input/"+str(i)+'.png'))
	if(i % 24 == 0):
		img.append(row)
		row = []
# vertically concatenates images
# of same width
newimg = concat_vh(img)

# show the output image
#cv2.imshow('test.jpg', newimg)
cv2.imwrite("output.jpg", newimg)
#cv2.waitKey()
