import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import math
path='./airplane.jpg'
image=img.imread(path)
airplane=image[:,:,0]
def sampling(image,size):
    row,col=image.shape
    row_new=int(row*size)
    col_new=int(col*size)

    air_new=np.empty((row_new,col_new))

    idxrow=np.linspace(0,row-1,row_new)
    idxrow_old=idxrow.astype(int)

    idxcol=np.linspace(0,col-1,col_new)
    idxcol_old=idxcol.astype(int)

    for i in range(row_new):
        for j in range(col_new):
            air_new[i,j]=airplane[idxrow_old[i],idxcol_old[j]]
    plt.imshow(image,cmap='gray')
    plt.title('original')
    plt.show()
    plt.imshow(air_new,cmap='gray')
    plt.title('orginal->')
    plt.show
sampling(이미지, 축소크기)
