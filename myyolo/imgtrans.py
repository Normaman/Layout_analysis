import os
import cv2

dataDir = "E:/dataset/images/train/"
saveDir = "E:/dataset/images/train/"
if not os.path.exists(saveDir):
    os.makedirs(saveDir)
i=0
for one_pic in os.listdir(dataDir):
    one_path = dataDir + one_pic
    one_img = cv2.imread(one_path)
    new_path = saveDir + one_pic
    cv2.imwrite(new_path, one_img)
    i=i+1
    print(i)