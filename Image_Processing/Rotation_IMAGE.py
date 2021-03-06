import math
import matplotlib.pylab as plt
import matplotlib.image as img
import numpy as np
orginal=img.imread('/home/kim/server/lenna1.png') #이미지 불러오기
image=orginal[:,:,0] #원본이미지의 하나의채널만 사용
angle=int(input('바꿀 각도'))

def padding(image,angle): #
        rows,cols=image.shape #원본 이미지의 크기
        ceta=math.radians(angle)
        ceta_nine=math.radians(90-angle)
        width=abs(cols*math.cos(ceta_nine)) + abs(rows* math.cos(ceta))  # 회전시켯을때의 세로 길이
        height=abs(cols*math.cos(ceta)) + abs(rows*math.cos(ceta_nine))# 회전시켰을때의 가로 길이

        padding_rows=np.round(height).astype(int) #실수값이므로 정수형 int로 변환
        padding_cols=np.round(width).astype(int)
        if angle %180 ==0:
                k=np.zeros((rows,cols))
        else:
                k=np.zeros((padding_rows,padding_cols)) #회전시켰을때 가로의 길이와 세로의 길이만큼 배열 생성
        row,col=k.shape #padding생성한 이미지의 크기
        a=int((row-rows)/2)
        b=int((col-cols)/2)
        k[row-rows-a:row-rows-a+rows,col-cols-b:col-cols-b+cols]=image #원본이미지는 가운데 놓고 나머지부분을 0으로 처리
        return k , row, col
def rotation(pad,angle):

        angle1 = math.radians(angle)
        rot_matrix_inv = [[math.cos(angle1), math.sin(angle1)], [-math.sin(angle1), math.cos(angle1)]]
        mid_x=math.ceil((row+1)/2)
        mid_y=math.ceil((col+1)/2)
        k=np.copy(pad)
        for i in range(row):
                for j in range(col):
                        new_xy= np.array([j,row-1-i])
                        new_xy_shifted = new_xy - np.array([mid_x, mid_y])
                        old_xy_shifted = np.matmul(rot_matrix_inv, new_xy_shifted)
                        old_xy = old_xy_shifted + np.array([mid_x, mid_x])
                        old_pxl_r=row-1-old_xy[1]
                        old_pxl_c=old_xy[0]
                        old_pxl_r = np.round(old_pxl_r).astype(int)
                        old_pxl_c = np.round(old_pxl_c).astype(int)
                        if (old_pxl_r >= 0 and old_pxl_r < row) and (old_pxl_c >= 0 and old_pxl_c < col):
                                pad[i, j] = k[old_pxl_r,old_pxl_c]
        plt.imshow(pad,cmap='gray')
        plt.show()
pad,row,col=padding(image,angle)
rotation(pad,angle)

#