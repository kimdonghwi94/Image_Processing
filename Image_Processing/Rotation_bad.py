
import math
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
a=img.imread('/home/kim/server/lenna1.png')
a=a[:,:,0]
rows,cols=a.shape
angle=30

# k=np.zeros((rows+150,cols+150))
# k[k.shape[0]-rows-75:rows+75,k.shape[1]-cols-75:cols+75]=a

angle=angle / 180 *math.pi

l=np.copy(a)

rot_matrix_inv = [[math.cos(angle),math.sin(angle)],[-math.sin(angle),math.cos(angle)]]

mid_x=math.ceil((a.shape[0]+1)/2)
mid_y=math.ceil((a.shape[1]+1)/2)


for i in range(rows):
        for j in range(cols):

                new_xy= np.array([j,rows-1-i])

                new_xy_shifted = new_xy - np.array([mid_x, mid_y])
                old_xy_shifted = np.matmul(rot_matrix_inv, new_xy_shifted)
                old_xy = old_xy_shifted + np.array([mid_x, mid_x])

                old_pxl_r=rows-1-old_xy[1]
                old_pxl_c=old_xy[0]

                old_pxl_r = np.round(old_pxl_r).astype(int)
                old_pxl_c = np.round(old_pxl_c).astype(int)

                if (old_pxl_r >= 0 and old_pxl_r < rows) and (old_pxl_c >= 0 and old_pxl_c < cols):
                        l[i,j] = a[old_pxl_r,old_pxl_c]

plt.imshow(l)
plt.show()