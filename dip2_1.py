import cv2
import numpy as np
from dip2 import r
img = cv2.imread("C:\\Users\\Itesha\\Downloads\\image1.jpg")
img1 = cv2.imread("C:\\Users\\Itesha\\DSA201\\blk.jpg")

# print(np.shape(img),np.shape(img1))
# output (826, 611, 3) (826, 611, 3)
#print(np.shape(r))
crop = np.zeros([r[3]-r[1], r[2]-r[0], 3], dtype=np.uint8)
crop = img-img1

cv2.imwrite('crop.jpg', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()