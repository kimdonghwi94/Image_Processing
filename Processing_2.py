# import numpy as np
# import matplotlib.image as img
# import matplotlib.pyplot as plt
# lenna1 = img.imread('/home/kim/PycharmProjects/tensorflow2.0-gpu/donghwikim/imageclass/lenna1.png')
# lenna = lenna1[:, :, 0]
# print(lenna1)
# def blurring(lenna,mask_size):
#     mask1 = np.ones((mask_size, mask_size)) / mask_size ** 2
#     guard = int((mask_size - 1) / 2)
#     out = np.copy(lenna)
#     for i in range(guard, lenna.shape[0] - guard):
#         for j in range(guard, lenna.shape[1] - guard):
#             out[i, j] = np.sum(mask1 * lenna[i-guard:i + guard+1, j-guard:j + guard+1])
#     return out
# def sharp(out,mask_size):
#     medium = mask_size // 2
#     mask2 = -(mask_size * 2) * (np.ones((mask_size, mask_size)))
#     mask2[medium, medium] = (np.sum(mask2) * -1) * 2
#     mask2 = mask2 / np.sum(mask2)
#     out1 = np.copy(out)
#     guard = int((mask_size - 1) / 2)
#     for i in range(guard, lenna.shape[0] - guard):
#         for j in range(guard, lenna.shape[1] - guard):
#             out1[i, j] = np.sum(mask2 * out[i-guard:i + guard+1, j-guard:j + guard+1])
#     return out1
# out=blurring(lenna,5)
# out1=sharp(out,5)
# out2=sharp(lenna,5)
#
# plt.imshow(lenna1, cmap='gray')  # 원본
# plt.show()
# plt.imshow(out, cmap='gray')  # 흐릿하게한것
# plt.show()
# plt.imshow(out1, cmap='gray')  # 흐릿하게 한거에서 선명하게
# plt.show()
# plt.imshow(out2,cmap='gray') #원본에서 선명하게
# plt.show()

# def erosion(lenna,mask_size): #침식
#     mask1 = np.ones((mask_size, mask_size),np.float32)
#     guard = int((mask_size - 1) / 2)
#     out = np.copy(lenna)
#     for i in range(guard, lenna.shape[0] - guard):
#         for j in range(guard, lenna.shape[1] - guard):
#             out[i, j] = np.max(lenna[i - guard:i - guard + mask_size, j - guard:j - guard + mask_size] * mask1)
#     lenna=out
#     return lenna
#
# def dilation(lenna,mask_size): #팽창
#     mask1 = np.ones((mask_size, mask_size),np.float32)
#     guard = int((mask_size - 1) / 2)
#     out = np.copy(lenna)
#     for i in range(guard, lenna.shape[0] - guard):
#         for j in range(guard, lenna.shape[1] - guard):
#             out[i, j] = np.min(lenna[i - guard:i - guard + mask_size, j - guard:j - guard + mask_size] * mask1)
#     lenna=out
#     return lenna


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as img

#dir = '/home/kim/PycharmProjects/tensorflow2.0-gpu/lenna1.png'
#a = img.imread(dir)
#def expand(image,n):
   # c = np.zeros((int(image.shape[0] * n), (image.shape[1] * n)))
   # for i in range(image.shape[0] ):
      #  for j in range(image.shape[1]):
         #   c[i*n:i*n+n,j*n:j*n+n]=image[i,j,0]
  #  plt.imshow(image)
  #  plt.title('original')
   # plt.show()
   # plt.imshow(c,cmap='gray')
   # plt.title('expand')
  #  plt.show()
#expand(a,1.5)
a=img.imread('./airplane.jpg')
a=a[:,:,0]
print(a.shape)
def sampling(image,size):
    c=np.zeros((int(image.shape[0]/2),int(image.shape[1]/2)))
    print(c.shape)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            print(i,j)
            c[i,j]=np.max(image[i*size:i*size+size,j*size:j*size+size])
    plt.imshow(c)
    plt.show()
sampling(a,2)

