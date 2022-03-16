import cv2

photo = "aaa.jpg"
img = cv2.imread(photo)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted_img = 255-gray_img

blurred_img = cv2.GaussianBlur(inverted_img,(21,21), 0)

inverted_blurred_img = 255-blurred_img

pencil_sketch = cv2.divide(gray_img,inverted_blurred_img,scale=256.0)

cv2.imwrite("sketch2.png",pencil_sketch)



