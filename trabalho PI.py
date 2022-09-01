from PIL import Image
import numpy as np

def showImage(array):
    pil_image=Image.fromarray(array)
    pil_image.show()
    pil_image.save('ratofinal.png')

def bilinearInterpolation(img):
    ar = np.array(img)

    h, l = ar.shape
    hNew = h*2 - 1
    lNew = l*2 -1

    B = np.zeros((hNew, lNew))
    B[0:hNew:2, 0:lNew:2] = ar[0:h, 0:l]
    print(B)
    
    B = B.astype(np.uint8)
    pil_image=Image.fromarray(B)
    #pil_image.show()
    pil_image.save('ratofinal.png')

    #B.save('bilinear-rato.png')
    showImage(B)

img = Image.open(r"/home/marc/Documents/UFT/5 PERIODO/Processamento de Imagens/trab PI/rato.jpg").convert('L')
img.save('rato-greyscale.png')
#ar = np.array(img)

bilinearInterpolation(img)

#showImage(ar)

#for element in ar:
#    print(element)