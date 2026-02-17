from PIL import Image
import numpy as np
from random import randint

r = float(input('Write a resolution. '))
DPL_const = 2/r
DPL = DPL_const
num = 0

min_rand_DPL = int(input('Write a chance how blow up DPL. '))

X = int(input('Write x. '))
Y = int(input('Write y. '))
B = X*Y

picture = np.ones((Y, X, 3), dtype=np.uint8)

print(DPL)
count = 0

for index in range(B):
    print(num)
    y = index // X
    x = index % X
    
    if num >= 1:
        picture[y, x] = [255, 255, 255]
        num -= 1
    else:
        num += DPL
    DPL = DPL_const * randint(1, min_rand_DPL)

img = Image.fromarray(picture, 'RGB')
img.save('DrainTube.png')
