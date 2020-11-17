from PIL import Image
import os, cv2
import numpy as np
import random

img_dir = 'archive'
new_dir = 'images'
base_dir = os.getcwd()

for name in os.listdir(img_dir):
    old = os.path.join(img_dir,name)
    if name[1] == '1':
        name = '10'
    elif name[1] == '2':
        name = '20'
    elif name[1] == '3':
        name = '30'
    elif name[1] == '4':
        name = '40'
    elif name[1] == '5':
        name = '50'
    else:
        name = '60'

    new = os.path.join(new_dir,name)
    # tmp = cv2.imread(os.path.join(img, os.listdir(img)[0]))
    if os.path.isdir(new):
        count = len(os.listdir(new))
    else:
        count = 0

    if not os.path.isdir(os.path.join(base_dir, new)):
        os.mkdir(os.path.join(base_dir, new))

    images = os.listdir(old)
    images = random.sample(images, 20)
    # print(image)
    for f in images:
        count += 1
        old_img = os.path.join(old,f)
        # name, ext = os.path.splitext(f)
        new_img = os.path.join(new,str(count))
        # print(old_img)
        # print(new_img)
        # print()
        tmp = Image.open(os.path.join(base_dir,old_img))
        tmp_numpy = np.array(tmp, 'uint8')
        gray = cv2.cvtColor(tmp_numpy, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(os.path.join(base_dir,new_img + '.jpg'), gray)

        # tmp.save(os.path.join(base_dir,new_img + '.jpg'))
        # tmp = Image.open(base_dir + '/' + old_img)
        # tmp.save(base_dir + '/' + new_img)
        
