import cv2
# Parameters
source = "Nishant.jpeg" #Image file link
destination = "newImg.png"  #name of the resized file
scale_percent = 50
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)  used to open and see the file

n_width = int(src.shape[1] * scale_percent /100)
n_height = int(src.shape[0] * scale_percent /100)

output = cv2.resize(src, (n_width, n_height))

cv2.imwrite(destination, output)
# cv2.waitKey(0)  used with imshow 