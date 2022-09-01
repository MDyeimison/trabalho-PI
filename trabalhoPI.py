import numpy as np
from PIL import Image

def resizeImage(img):
    source = Image.open(img)

    original = np.asarray(source)
    rows, cols, layers = original.shape
    new = np.zeros((2*rows - 1, 2*cols - 1, layers))
    print("original dimensions: ", original.shape)

    for layer in range(3):
        new[:, :, layer] = resizeLayer(original[:, :, layer])

    #convert float to int
    new = new.astype(np.uint8)
    print("     new dimensions: ", new.shape)

    result = Image.fromarray(new)
    newimg = "new-" + img
    result.save(newimg)

def resizeLayer(original):
    rows, cols = original.shape

    rNew = 2*rows - 1
    cNew = 2*cols -1

    new = np.zeros((rNew, cNew))
    #moving points
    new[0:rNew:2, 0:cNew:2] = original[0:rows, 0:cols]

    #column values
    new[1:rNew:2, :] = (new[0:rNew-1:2, :] + new[2:rNew:2, :]) / 2
    #rown values
    new[:, 1:cNew:2] = (new[:, 0:cNew-1:2] + new[:, 2:cNew:2]) / 2

    return new


img = "rato.jpg"
resizeImage(img)