import cv2
import time

name = 'Daniel' #replace with your name

cam = cv2.VideoCapture(0)

img_counter = 0

for i in range(30):
    time.sleep(1)
    ret, frame = cam.read()
    img_name = "dataset/"+ name +"/image_{}.jpg".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1

cam.release()

