import numpy as np
from PIL import Image

# Create 3d numpy array of zeros, then replace zeros (black pixels) with yellow pxls
data = np.zeros((5,4,3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)

#make a red patch
data[1:4, 0:1] = [255, 0, 255]
data[1:4, 3:4] = [0, 0, 255]
data[0:1, 1:3] = [0, 255, 0]
data[4:5, 1:3] = [140, 0, 0]
data[2, 2] = [140, 30, 200]

img = Image.fromarray(data, "RGB")
img.save('canvas.png')