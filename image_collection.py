#!/usr/bin/env python3
# Import opencv
import cv2

# Import uuid
import uuid

# Import Operating System
import os

# Import time
import time

# Defining Variables
labels = ['Quadrilateral']
number_imgs = 2
IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')

# Creating Directories
if not os.path.exists(IMAGES_PATH):
    if os.name == 'posix':
        os.mkdirs(f"{IMAGES_PATH}")
    if os.name == 'nt':
        os.mkdirs(f"{IMAGES_PATH}")
for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(path):
        os.mkdir(f"{path}")

# Images Collection
for label in labels:
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    cTime = time.time()
    target_time = cTime + 2
    collected_images = 0

    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cTime = time.time()
        if cTime > target_time:
            imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
            print('Collecting image {}'.format(imgname))
            cv2.imwrite(imgname, frame)
            target_time = cTime + 2
            collected_images += 1

        if collected_images >= number_imgs:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
