import math
import matplotlib.pylab as plt
import matplotlib.image as img
import numpy as np
orginal=img.imread('./lenna.png') #이미지 불러오기
image=orginal[:,:,0] #원본이미지의 하나의채널만 사용
angle=int(input('옮길각도 '))

def padding(image,angle): #
        rows,cols=image.shape #원본 이미지의 크기
        ceta=math.radians(angle)
        ceta_nine=math.radians(90-angle)
        width=abs(cols*math.cos(ceta_nine)) + abs(rows* math.cos(ceta))
        height=abs(cols*math.cos(ceta)) + abs(rows*math.cos(ceta_nine))
        padding_rows=np.ceil(height).astype(int) #실수값이므로 정수형 int로 변환
        padding_cols=np.ceil(width).astype(int)
        if rows==padding_rows or padding_cols == cols: #정사각형일때
                row=padding_rows
                col=padding_cols
        else:                                           #직사각형일때
                row=padding_cols
                col=padding_rows
        ifrow = abs(rows - row)
        ifcol = abs(cols - col)
        if rows>row :
                k=np.zeros((row+ifrow,col))
        elif cols>col:
                k=np.zeros((row,col+ifcol))
        else:
                k=np.zeros((row,col))
        row,col=k.shape
        a = int((row - rows) / 2)
        b = int((col - cols) / 2)
        k[row-rows-a:row-rows-a+rows,col-cols-b:col-cols-b+cols]=image #원본이미지는 가운데 놓고 나머지부분을 0으로 처리
        plt.imshow(k,cmap='gray')
        plt.show()
        return k
def rotation(pad,angle):
        row,col=pad.shape #패딩을 넣은 이미지 사이즈
        angle1 = math.radians(angle)
        rot_matrix_inv = [[math.cos(angle1), math.sin(angle1)], [-math.sin(angle1), math.cos(angle1)]]
        if row==col: #정사각형일때 중심
                mid_x=math.ceil(row)/2
                mid_y=math.ceil(col)/2
        else:        #직사각형일때 중심
                mid_x = math.ceil(col / 2)
                mid_y = math.ceil(row / 2)
        k=np.copy(pad)
        for i in range(row):
                for j in range(col):
                        new_xy= np.array([j,row-i])

                        new_xy_shifted = new_xy - np.array([mid_x, mid_y])
                        old_xy_shifted = np.matmul(rot_matrix_inv, new_xy_shifted)
                        old_xy = old_xy_shifted + np.array([mid_x, mid_y])

                        old_pxl_r=row-old_xy[1]
                        old_pxl_c=old_xy[0]

                        old_pxl_r = np.round(old_pxl_r).astype(int)
                        old_pxl_c = np.round(old_pxl_c).astype(int)

                        if (old_pxl_r >= 0 and old_pxl_r < row) and (old_pxl_c >= 0 and old_pxl_c < col):
                                pad[i, j] = k[old_pxl_r,old_pxl_c]
        plt.imshow(pad,cmap='gray')
        plt.show()
        return pad
padiing = padding(image,angle)
rotation(padiing,angle)
